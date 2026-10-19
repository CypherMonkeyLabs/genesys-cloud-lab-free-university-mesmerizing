try {
  var s = JSON.parse(localStorage.getItem('gccx-settings') || '{}');
  var theme = s.theme || "bloom";
  if (theme === "paper" || theme === "harbor") theme = "bloom";
  document.documentElement.dataset.theme = theme;
  if (s.font) document.documentElement.dataset.font = s.font;
  if (s.reduce || window.matchMedia('(prefers-reduced-motion: reduce)').matches) document.documentElement.dataset.reduce = '1';
  var narrow = window.matchMedia('(max-width: 700px)').matches;
  document.documentElement.style.setProperty('--chrome-h', narrow ? '56px' : '64px');
  document.documentElement.style.setProperty('--bar-h', '64px');
} catch (e) {}
