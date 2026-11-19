/* Sada-e-Rehmat — motion + interactions. No dependencies. */
(() => {
  const doc = document.documentElement;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  let vh = window.innerHeight;

  /* ---------- Navigation ---------- */
  const nav = $('.nav');
  const toggle = $('.nav-toggle');
  let lastY = window.scrollY;
  if (toggle) {
    toggle.addEventListener('click', () => {
      const open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    $$('.nav-links a').forEach(a => a.addEventListener('click', () => {
      document.body.classList.remove('menu-open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }
  const onNav = () => {
    const y = window.scrollY;
    if (!nav) return;
    nav.classList.toggle('is-scrolled', y > 24);
    const goingDown = y > lastY && y > 400;
    if (!document.body.classList.contains('menu-open')) nav.classList.toggle('is-hidden', goingDown);
    lastY = y;
  };

  /* ---------- Split helpers ---------- */
  $$('[data-lines]').forEach(el => {
    $$('.ln > span', el).forEach((s, i) => s.style.setProperty('--i', i));
  });
  $$('[data-stagger]').forEach(group => {
    $$('[data-reveal]', group).forEach((el, i) => el.style.setProperty('--i', i % 6));
  });

  /* ---------- Reveal on scroll ---------- */
  const revealEls = $$('[data-reveal], [data-lines], [data-clip]');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });
    revealEls.forEach(el => io.observe(el));
  } else revealEls.forEach(el => el.classList.add('in'));

  /* ---------- Count up ---------- */
  const counters = $$('[data-count]');
  const runCount = el => {
    const end = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const dur = 1600; const t0 = performance.now();
    const fmt = n => Math.round(n).toLocaleString('en-GB') + suffix;
    if (reduce) { el.textContent = fmt(end); return; }
    const tick = t => {
      const k = clamp((t - t0) / dur);
      const e = 1 - Math.pow(1 - k, 4);
      el.textContent = fmt(end * e);
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); } }), { threshold: 0.6 });
    counters.forEach(c => co.observe(c));
  } else counters.forEach(runCount);

  /* ---------- Scroll-linked scenes ---------- */
  const cines = $$('.cine');
  const heroes = $$('.page-hero:not(.page-hero-plain)');
  const parallax = $$('[data-parallax]');
  const zooms = $$('.media-zoom, .cta');
  const stacks = $$('.stack-card');
  const hss = $$('.hs');
  const chapters = $$('.chapter');
  const wide = () => window.matchMedia('(min-width: 761px)').matches;

  const sizeHs = () => {
    hss.forEach(hs => {
      const track = $('.hs-track', hs);
      if (!track) return;
      if (!wide() || reduce) { hs.style.removeProperty('--hs-h'); track.style.transform = ''; return; }
      const dist = Math.max(0, track.scrollWidth - window.innerWidth);
      hs._dist = dist;
      hs.style.setProperty('--hs-h', (dist + vh) + 'px');
    });
  };

  const frame = () => {
    const y = window.scrollY;
    onNav();
    if (reduce) return;

    cines.forEach(c => {
      const r = c.getBoundingClientRect();
      const p = clamp(-r.top / (r.height - vh));
      const f = $('.cine-sticky', c);
      f.style.setProperty('--p', p.toFixed(4));
      $$('.cine-frame, .cine-a, .cine-b, .scroll-cue', c).forEach(n => n.style.setProperty('--p', p.toFixed(4)));
    });

    heroes.forEach(h => {
      const r = h.getBoundingClientRect();
      if (r.bottom < 0) return;
      h.style.setProperty('--p', clamp(-r.top / r.height).toFixed(4));
    });

    parallax.forEach(m => {
      const r = m.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      const center = r.top + r.height / 2 - vh / 2;
      m.style.setProperty('--py', (center * -0.06).toFixed(2));
    });

    zooms.forEach(m => {
      const r = m.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      m.style.setProperty('--z', clamp((vh - r.top) / (vh + r.height * .4)).toFixed(4));
    });

    if (wide()) {
      stacks.forEach((card, i) => {
        const next = stacks[i + 1];
        if (!next) { card.style.setProperty('--s', 1); card.style.setProperty('--dim', 0); return; }
        const top = parseFloat(getComputedStyle(card).top) || 0;
        const nr = next.getBoundingClientRect();
        const k = clamp(1 - (nr.top - top) / (vh * .9));
        card.style.setProperty('--s', (1 - k * 0.06).toFixed(4));
        card.style.setProperty('--dim', (k * 0.25).toFixed(3));
      });

      hss.forEach(hs => {
        const r = hs.getBoundingClientRect();
        const total = r.height - vh;
        const p = total > 0 ? clamp(-r.top / total) : 0;
        const track = $('.hs-track', hs);
        track.style.transform = `translate3d(${(-p * (hs._dist || 0)).toFixed(1)}px,0,0)`;
        const bar = $('.hs-progress', hs);
        if (bar) bar.style.setProperty('--hp', p.toFixed(4));
      });
    }

    chapters.forEach(ch => {
      const r = ch.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const c = clamp(1 - r.top / vh);
      $('.chapter-sticky', ch).style.setProperty('--c', c.toFixed(4));
    });

  };

  let ticking = false;
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { frame(); ticking = false; }); } };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', () => { vh = window.innerHeight; sizeHs(); frame(); });
  window.addEventListener('load', () => { sizeHs(); frame(); });
  sizeHs(); frame();

  /* ---------- Segmented controls ---------- */
  const placeThumb = seg => {
    const on = $('button[aria-pressed="true"]', seg);
    const thumb = $('.thumb', seg);
    if (!on || !thumb) return;
    thumb.style.width = on.offsetWidth + 'px';
    thumb.style.transform = `translateX(${on.offsetLeft}px)`;
  };
  $$('.seg').forEach(seg => {
    if (!$('.thumb', seg)) { const t = document.createElement('span'); t.className = 'thumb'; seg.prepend(t); }
    $$('button', seg).forEach(b => b.addEventListener('click', () => {
      $$('button', seg).forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      placeThumb(seg);
      seg.dispatchEvent(new CustomEvent('change', { detail: b.dataset.value }));
    }));
    requestAnimationFrame(() => placeThumb(seg));
  });
  window.addEventListener('resize', () => $$('.seg').forEach(placeThumb));
  if (document.fonts) document.fonts.ready.then(() => $$('.seg').forEach(placeThumb));

  /* ---------- Package explorer ---------- */
  const explorer = $('[data-explorer]');
  if (explorer) {
    const store = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} } };
    const savedCur = store.get('ser-cur');
    const state = { room: store.get('ser-room') || 'quad', cur: savedCur === 'usd' ? 'usd' : 'gbp', route: 'all' };
    const fmtGBP = n => '£' + Number(n).toLocaleString('en-GB');
    const fmtUSD = n => '$' + Number(n).toLocaleString('en-US');
    const fmt = (n, c) => c === 'gbp' ? fmtGBP(n) : fmtUSD(n);
    const tween = (el, to, cur) => {
      const from = parseFloat(el.dataset.v || 0);
      el.dataset.v = to;
      if (reduce || !from || el.dataset.c !== cur) { el.textContent = fmt(to, cur); el.dataset.c = cur; return; }
      el.dataset.c = cur;
      const t0 = performance.now(), dur = 600;
      const step = t => {
        const k = clamp((t - t0) / dur); const e = 1 - Math.pow(1 - k, 3);
        const v = from + (to - from) * e;
        el.textContent = fmt(Math.round(v / 5) * 5, cur);
        if (k < 1) requestAnimationFrame(step); else el.textContent = fmt(to, cur);
      };
      requestAnimationFrame(step);
    };
    const render = () => {
      const other = state.cur === 'gbp' ? 'usd' : 'gbp';
      $$('[data-price]').forEach(card => {
        const d = card.dataset;
        const main = $('.amount', card); const alt = $('.alt', card); const lbl = $('.room-label', card);
        tween(main, +d[state.room + state.cur.charAt(0).toUpperCase() + state.cur.slice(1)], state.cur);
        alt.textContent = '≈ ' + fmt(d[state.room + other.charAt(0).toUpperCase() + other.slice(1)], other);
        if (lbl) lbl.textContent = { quad: 'Quad room', triple: 'Triple room', double: 'Double room' }[state.room] + ' · per person';
      });
      $$('[data-cell]').forEach(td => {
        const [room] = td.dataset.cell.split(':');
        td.textContent = fmt(td.dataset[state.cur], state.cur);
        td.closest('table').querySelectorAll('th[data-room]').forEach(th => th.style.color = th.dataset.room === state.room ? 'var(--ink)' : '');
        td.style.fontWeight = room === state.room ? '600' : '400';
      });
      $$('[data-addon]').forEach(td => { td.textContent = fmt(td.dataset[state.cur], state.cur); });
      $$('.tier-sec').forEach(sec => {
        let shown = 0;
        $$('.pkg', sec).forEach(p => {
          const ok = state.route === 'all' || p.dataset.route === state.route;
          p.classList.toggle('is-out', !ok); if (ok) shown++;
        });
        const note = $('.empty-note', sec); if (note) note.classList.toggle('show', shown === 0);
      });
      $$('.compare tbody tr').forEach(tr => { tr.style.display = state.route === 'all' || tr.dataset.route === state.route ? '' : 'none'; });
      renderCompare();
    };

    /* Compare up to three journeys side by side */
    const cmpData = (() => { try { return JSON.parse($('#cmp-data').textContent); } catch (e) { return []; } })();
    const byId = Object.fromEntries(cmpData.map(p => [p.id, p]));
    const slots = $$('.cmp-pick select');
    const grid = $('.cmp-grid');
    const ROOMS = ['quad', 'triple', 'double'];
    const ROWS = [['Length', p => p.days], ['Arrive', p => p.arrive], ['Depart', p => p.depart],
      ['Makkah hotel', p => p.makkah], ['Makkah dates', p => p.makkahDates], ['Madinah hotel', p => p.madinah], ['Madinah dates', p => p.madinahDates],
      ['Aziziya', p => p.aziziya], ['Hajj days', () => 'Maktab A · Zone 1 · 14–18 May'], ['Train', p => 'Haramain · ' + p.train], ['Madinah upgrade', p => p.upgrade]];
    function renderCompare() {
      if (!grid || !slots.length) return;
      const picks = slots.map(s => byId[s.value]).filter(Boolean);
      const ri = ROOMS.indexOf(state.room);
      const roomName = { quad: 'Quad', triple: 'Triple', double: 'Double' }[state.room];
      const other = state.cur === 'gbp' ? 'usd' : 'gbp';
      grid.innerHTML = picks.map(p => {
        const rows = ROWS.map(([label, get]) => {
          const diff = picks.length > 1 && new Set(picks.map(get)).size > 1;
          return `<div class="${diff ? 'diff' : ''}"><dt>${label}</dt><dd>${get(p)}</dd></div>`;
        }).join('');
        return `<article class="cmp-col" style="--dot:var(--t-${p.tid})">
          <div class="cmp-head"><small>${p.tier} · ${p.route}</small><h3>${p.name}</h3></div>
          <div class="cmp-price"><small>${roomName} room · per person</small><div class="amount">${fmt(p[state.cur][ri], state.cur)}</div><small>≈ ${fmt(p[other][ri], other)}</small></div>
          <dl class="cmp-rows">${rows}</dl>
          <a class="btn" href="contact.html?package=${p.id}">Enquire about ${p.name}</a>
        </article>`;
      }).join('');
      $$('[data-compare]').forEach(b => b.classList.toggle('on', slots.some(s => s.value === b.dataset.compare)));
    }
    slots.forEach(s => s.addEventListener('change', renderCompare));
    let nextSlot = 0;
    $$('[data-compare]').forEach(b => b.addEventListener('click', () => {
      const id = b.dataset.compare;
      if (!slots.some(s => s.value === id)) { slots[nextSlot % slots.length].value = id; nextSlot++; }
      renderCompare();
      const target = $('#compare');
      if (target) target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    }));
    const sync = (name, val) => {
      $$(`.seg[data-name="${name}"] button`).forEach(b => b.setAttribute('aria-pressed', String(b.dataset.value === val)));
      $$(`.seg[data-name="${name}"]`).forEach(placeThumb);
    };
    sync('room', state.room); sync('cur', state.cur); sync('route', state.route);
    $$('.seg[data-name]').forEach(seg => seg.addEventListener('change', e => {
      state[seg.dataset.name] = e.detail;
      if (seg.dataset.name !== 'route') store.set('ser-' + seg.dataset.name, e.detail);
      sync(seg.dataset.name, e.detail);
      render();
    }));
    render();

    // Highlight tier tab for the section in view
    const tabs = $$('.tier-tabs a');
    if (tabs.length && 'IntersectionObserver' in window) {
      const so = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) tabs.forEach(t => t.classList.toggle('active', t.getAttribute('href') === '#' + e.target.id));
      }), { rootMargin: '-40% 0px -55% 0px' });
      $$('.tier-sec').forEach(s => so.observe(s));
    }
  }

  /* ---------- Contact: prefill package ---------- */
  const pkgSelect = $('#package');
  if (pkgSelect) {
    const want = new URLSearchParams(location.search).get('package');
    if (want) {
      const opt = Array.from(pkgSelect.options).find(o => o.value === want);
      if (opt) pkgSelect.value = want;
      const cat = $('#category'); if (cat) cat.value = 'Hajj';
    }
  }

  /* ---------- FAQ: one open at a time, smooth height ---------- */
  $$('.faq details').forEach(d => {
    const s = $('summary', d); const a = $('.ans', d);
    s.addEventListener('click', e => {
      if (reduce || !a.animate) return;
      e.preventDefault();
      if (d.open) {
        const h = a.offsetHeight;
        a.animate([{ height: h + 'px', opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 380, easing: 'cubic-bezier(.16,1,.3,1)' }).onfinish = () => { d.open = false; };
      } else {
        d.open = true;
        const h = a.offsetHeight;
        a.animate([{ height: '0px', opacity: 0 }, { height: h + 'px', opacity: 1 }], { duration: 520, easing: 'cubic-bezier(.16,1,.3,1)' });
      }
    });
  });

  /* ---------- Cookie notice ---------- */
  const cookie = $('#cookie');
  if (cookie) {
    let choice = null;
    try { choice = localStorage.getItem('ser-cookie'); } catch (e) {}
    if (!choice) setTimeout(() => cookie.classList.add('show'), 1400);
    $$('[data-cookie]', cookie).forEach(b => b.addEventListener('click', () => {
      try { localStorage.setItem('ser-cookie', b.dataset.cookie); } catch (e) {}
      cookie.classList.remove('show');
    }));
  }

  /* ---------- Scrolly: pinned stage, steps scroll past ---------- */
  $$('.scrolly').forEach(sc => {
    const steps = $$('.scrolly-step', sc);
    const frames = $$('.scrolly-frame', sc);
    const count = $('.scrolly-hud .count b', sc);
    const label = $('.scrolly-hud .label', sc);
    const bar = $('.scrolly-bar', sc);
    let current = -1;
    const set = i => {
      if (i === current || i < 0) return;
      current = i;
      steps.forEach((s, j) => s.classList.toggle('on', j === i));
      const target = steps[i].dataset.frame != null ? +steps[i].dataset.frame : i;
      frames.forEach((f, j) => f.classList.toggle('on', j === target));
      if (count) count.textContent = String(i + 1).padStart(2, '0');
      if (label) label.textContent = steps[i].dataset.label || '';
    };
    set(0);
    const pick = () => {
      const mid = window.innerWidth <= 860 ? vh * 0.62 : vh * 0.5;
      let best = 0;
      steps.forEach((s, j) => { if (s.getBoundingClientRect().top < mid) best = j; });
      set(best);
      if (bar) {
        const r = sc.getBoundingClientRect();
        bar.style.setProperty('--sp', clamp((vh * .5 - r.top) / r.height).toFixed(3));
      }
    };
    window.addEventListener('scroll', () => requestAnimationFrame(pick), { passive: true });
    pick();
  });

  /* ---------- Guides: reading progress + contents rail ---------- */
  const rp = $('.read-progress');
  const body = $('.guide-body');
  if (rp && body) {
    const links = $$('.guide-rail nav a');
    const secs = links.map(a => $(a.getAttribute('href'))).filter(Boolean);
    const upd = () => {
      const r = body.getBoundingClientRect();
      rp.style.setProperty('--rp', clamp(-r.top / (r.height - vh * .6)).toFixed(4));
      let cur = 0;
      secs.forEach((s, i) => { if (s.getBoundingClientRect().top < vh * .3) cur = i; });
      links.forEach((a, i) => a.classList.toggle('active', i === cur));
    };
    window.addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true });
    upd();
  }

  /* ---------- Guides hub filter ---------- */
  const hub = $('.hub-filter');
  if (hub) {
    $$('button', hub).forEach(b => b.addEventListener('click', () => {
      $$('button', hub).forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      const cat = b.dataset.cat;
      $$('.guide-card[data-cat]').forEach(c => c.classList.toggle('is-out', cat !== 'all' && c.dataset.cat !== cat));
    }));
  }

  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
})();
