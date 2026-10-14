// Progressive enhancement: content stays visible without JavaScript or motion support.
let dispose = () => {};
export function initMotion(root, language) {
  dispose();
  const cleanups = [];
  dispose = () => cleanups.splice(0).forEach(fn => fn());
  if (!root || document.body.classList.contains('admin-surface')) return;
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  if (preference.matches) return;
  const stop = () => {
    dispose();
    root.querySelectorAll('.motion-enter').forEach(el => el.classList.remove('motion-enter'));
  };
  preference.addEventListener('change', stop, {once: true});
  cleanups.push(() => preference.removeEventListener('change', stop));
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('motion-in');
      observer.unobserve(entry.target);
    }), {threshold: 0.06});
    cleanups.push(() => observer.disconnect());
    root.querySelectorAll('.hero-copy > *, .hero-visual, .section-head, .service-card, .steps > article, .comparison-card, .sample-project, .offer-card, .editorial-image, .cta').forEach(el => {
      el.classList.remove('reveal');
      el.classList.add('motion-enter');
      el.style.setProperty('--motion-delay', `${Math.min([...el.parentElement.children].indexOf(el), 4) * 85}ms`);
      observer.observe(el);
    });
  }
  // Enhance only actual review grids, leaving empty-state invitations untouched.
  root.querySelectorAll('.grid').forEach(grid => {
    if (grid.children.length < 2 || ![...grid.children].every(el => el.matches('.review-card'))) return;
    const wrapper = document.createElement('div');
    wrapper.className = 'reviews-motion';
    const viewport = document.createElement('div');
    viewport.className = 'reviews-viewport';
    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'button outline reviews-toggle';
    toggle.setAttribute('aria-pressed', 'false');
    const label = paused => language === 'ar' ? (paused ? 'تشغيل حركة التقييمات' : 'إيقاف حركة التقييمات') : (paused ? 'Play review animation' : 'Pause review animation');
    toggle.textContent = label(false);
    grid.before(wrapper);
    wrapper.append(toggle, viewport);
    viewport.append(grid);
    grid.classList.add('reviews-track');
    const originals = [...grid.children];
    originals.forEach(card => {
      const copy = card.cloneNode(true);
      copy.setAttribute('aria-hidden', 'true');
      copy.setAttribute('inert', '');
      grid.append(copy);
    });
    grid.style.setProperty('--review-duration', `${originals.length * 12}s`);
    let paused = false;
    toggle.onclick = () => {
      paused = !paused;
      wrapper.classList.toggle('is-paused', paused);
      toggle.textContent = label(paused);
      toggle.setAttribute('aria-pressed', String(paused));
    };
    cleanups.push(() => {
      originals.forEach(card => grid.append(card));
      [...grid.children].filter(card => !originals.includes(card)).forEach(card => card.remove());
      grid.classList.remove('reviews-track');
      wrapper.replaceWith(grid);
    });
  });
}
