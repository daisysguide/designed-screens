(function () {
  const pages = ['01-swipeable-intro.html', '02-onboarding-quiz.html', '03-building-your-plan.html', '04-sign-up.html', '05-otp-verification.html', '06-log-in.html', '07-personalized-results.html', '08-paywall.html', '09-partner-linking.html', '10-home.html', '11-progress.html', '12-settings.html', '13-topic-list.html', '14-manage-topics.html', '15-topic-intro.html', '16-topic-article.html', '17-question.html', '18-waiting-for-partner.html', '19-alignment-reveal.html', '20-post-reveal-reflection.html', '21-re-answer-flow.html', '22-completed-topic.html', '23-prediction-card.html', '24-empty-home.html', '25-empty-topic-list.html', '26-payment-failure.html', '27-connection-error.html', '28-onboarding-intro.html'];
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
