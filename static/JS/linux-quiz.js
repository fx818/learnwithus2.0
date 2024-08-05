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
  