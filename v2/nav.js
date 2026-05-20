(function () {
  const pages = ['01-swipeable-intro.html', '02-sign-up.html', '03-otp-verification.html', '04-log-in.html', '05-partner-linking.html', '06-onboarding-intro.html', '07-onboarding-quiz.html', '08-building-your-plan.html', '09-personalized-results.html', '10-customize-your-plan.html', '11-paywall.html', '12-home.html', '13-topic-list.html', '14-topic-intro.html', '15-topic-article.html', '16-question.html', '17-waiting-for-partner.html', '18-alignment-reveal.html', '19-post-reveal-reflection.html', '20-re-answer-flow.html', '21-completed-topic.html', '22-prediction-card.html', '23-progress.html', '24-settings.html', '25-empty-home.html', '26-empty-topic-list.html', '27-payment-failure.html', '28-connection-error.html'];
  const path = window.location.pathname.split('/').pop() || 'index.html';
  let idx = pages.indexOf(path);
  if (idx < 0) idx = 0;
  document.addEventListener('keydown', (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const tag = (e.target && e.target.tagName) || '';
    if (tag === 'INPUT' || tag === 'TEXTAREA') return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      if (idx < pages.length - 1) { e.preventDefault(); window.location.href = pages[idx + 1]; }
    }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      if (idx > 0) { e.preventDefault(); window.location.href = pages[idx - 1]; }
    }
  });
})();
