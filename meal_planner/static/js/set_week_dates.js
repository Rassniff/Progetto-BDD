// Imposta automaticamente le date della settimana corrente (Lun-Dom) nei campi di input
window.addEventListener('DOMContentLoaded', function() {
  const today = new Date();
  const dayOfWeek = today.getDay() === 0 ? 7 : today.getDay(); // Domenica = 7
  const monday = new Date(today);
  monday.setDate(today.getDate() - dayOfWeek + 1);
  const sunday = new Date(monday);
  sunday.setDate(monday.getDate() + 6);

  const startInput = document.getElementById('stats-week-start');
  const endInput = document.getElementById('stats-week-end');
  if (startInput && endInput) {
    startInput.value = monday.toISOString().slice(0, 10);
    endInput.value = sunday.toISOString().slice(0, 10);
  }
});