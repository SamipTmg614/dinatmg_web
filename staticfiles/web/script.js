const whatsappToggle = document.getElementById("whatsappToggle");
const messageBox = document.getElementById("messageBox");
const closeMessageBtn = document.getElementById("closeMessageBtn");
const sendMessageBtn = document.getElementById("sendMessageBtn");
const adminMessage = document.getElementById("adminMessage");

if (whatsappToggle && messageBox) {
  messageBox.classList.add("hidden");

  whatsappToggle.addEventListener("click", function () {
    const isHidden = messageBox.classList.contains("hidden");
    messageBox.classList.toggle("hidden", !isHidden);
    messageBox.setAttribute("aria-hidden", String(!isHidden));

    if (isHidden && adminMessage) {
      adminMessage.focus();
    }
  });

  messageBox.addEventListener("click", function (event) {
    if (event.target === messageBox) {
      messageBox.classList.add("hidden");
      messageBox.setAttribute("aria-hidden", "true");
    }
  });
}

if (closeMessageBtn && messageBox) {
  closeMessageBtn.addEventListener("click", function () {
    messageBox.classList.add("hidden");
    messageBox.setAttribute("aria-hidden", "true");
  });
}

if (sendMessageBtn && adminMessage && messageBox) {
  sendMessageBtn.addEventListener("click", function () {
    const text = adminMessage.value.trim();
    const whatsappNumber = whatsappToggle ? whatsappToggle.dataset.whatsappNumber : "";

    if (!text) {
      alert("Please write a message before sending.");
      adminMessage.focus();
      return;
    }

    if (!whatsappNumber) {
      alert("WhatsApp number is not configured.");
      return;
    }

    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(text)}`;
    window.open(whatsappUrl, "_blank", "noopener,noreferrer");

    adminMessage.value = "";
    messageBox.classList.add("hidden");
    messageBox.setAttribute("aria-hidden", "true");
  });
}

document.addEventListener("keydown", function (event) {
  if (event.key === "Escape" && messageBox && !messageBox.classList.contains("hidden")) {
    messageBox.classList.add("hidden");
    messageBox.setAttribute("aria-hidden", "true");
  }
});

const clickableBlogCards = document.querySelectorAll(".blog-list-card-clickable[data-url]");

clickableBlogCards.forEach(function (card) {
  card.addEventListener("click", function (event) {
    if (event.target.closest("a, button, input, textarea, form")) {
      return;
    }
    window.location.href = card.dataset.url;
  });

  card.addEventListener("keydown", function (event) {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      window.location.href = card.dataset.url;
    }
  });
});
