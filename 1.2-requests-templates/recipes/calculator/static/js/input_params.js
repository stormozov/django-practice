const servingsInput = document.getElementById('servings-input');
const updateButton = document.getElementById('update-button');
const urlParams = new URLSearchParams(window.location.search);

updateButton.addEventListener('click', () => {
    const servings = servingsInput.value;
    urlParams.set('servings', servings);
    window.location.href = `${window.location.pathname}?${urlParams.toString()}`;
});