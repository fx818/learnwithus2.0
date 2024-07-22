

function autoResizeTextarea(textarea) {
    textarea.style.height = 'auto'; // Reset the height
    textarea.style.height = textarea.scrollHeight + 'px'; // Set it to the scroll height
}

document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.getElementById('autoResizeTextarea');
    textarea.addEventListener('input', () => autoResizeTextarea(textarea));
});
