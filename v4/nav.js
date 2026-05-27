(function () {
  const pages = ['01-swipeable-intro.html', '02-onboarding-quiz.html', '03-building-your-plan.html', '04-sign-up.html', '05-otp-verification.html', '06-name-entry.html', '07-log-in.html', '08-personalized-results.html', '09-paywall.html', '10-partner-linking.html', '11-home.html', '12-progress.html', '13-settings.html', '14-topic-list.html', '15-manage-topics.html', '16-topic-intro.html', '17-topic-article.html', '18-question.html', '19-waiting-for-partner.html', '20-alignment-reveal.html', '21-post-reveal-reflection.html', '22-re-answer-flow.html', '23-completed-topic.html', '24-prediction-card.html', '25-empty-home.html', '26-empty-topic-list.html', '27-payment-failure.html', '28-connection-error.html', '29-onboarding-intro.html'];
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
