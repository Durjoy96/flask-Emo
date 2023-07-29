document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const loader = document.querySelector(".loader");
  const copyButtons = document.querySelectorAll(".copy-button");
  const closeButtons = document.querySelectorAll(".close-button");
  const copyNotification = document.querySelector(".copy-notification");
  const response = document.getElementById("#response");
  


  copyButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const bubbleContent = event.target.closest(".bubble-content");
      const textToCopy = bubbleContent.querySelector("p").innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        showCopyNotification();
      });
    });
  });

  closeButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const chatBubble = event.target.closest(".chat-bubble");
      chatBubble.style.display = "none";
    });
  });

  function showCopyNotification() {
    copyNotification.classList.remove("hidden");
    setTimeout(() => {
      copyNotification.classList.add("hidden");
    }, 2000);
  }


  form.addEventListener("submit", () => {
    loader.classList.add("show");
  });

// Scroll to the response section when the page loads with an answer
const answerElement = document.querySelector("#response .chat-bubble");
if (answerElement) {
    answerElement.scrollIntoView({ behavior: 'smooth' });
}
  });


// Scroll to the response section after page reloads with an answer
window.onload = () => {
const answerElement = document.querySelector("#response .chat-bubble");
if (answerElement) {
    answerElement.scrollIntoView({ behavior: 'smooth' });
}
};

