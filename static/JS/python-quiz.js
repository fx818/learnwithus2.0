function toggleAnswer(id, answer, btn) {
  var element = document.getElementById("answer-" + id);

  if (element.innerText.includes("(Hidden)")) {
    element.innerText = "ans) " + answer;
    element.style.fontWeight = "bold";
    btn.innerText = "Hide Answer";
  } else {
    element.innerText = "ans) (Hidden)";
    element.style.fontWeight = "normal";
    btn.innerText = "Reveal Answer";
  }
}


// for color changing effect on the left side
const items = document.querySelectorAll("main .left p");

function removeActiveClasses() {
  items.forEach((item) => {
    item.classList.remove("active");
  });
}

function setActiveItem(item) {
  removeActiveClasses();
  item.classList.add("active");
  localStorage.setItem("activeItem", item.id);
}

items.forEach((item) => {
  item.addEventListener("click", function () {
    setActiveItem(this);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const activeItemId = localStorage.getItem("activeItem");
  if (activeItemId) {
    const activeItem = document.getElementById(activeItemId);
    if (activeItem) {
      setActiveItem(activeItem);
    }
  }
});
