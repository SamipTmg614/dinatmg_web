const messageToggle = document.getElementById("messageToggle");
const messageBox = document.getElementById("messageBox");
const closeMessageBtn = document.getElementById("closeMessageBtn");
const sendMessageBtn = document.getElementById("sendMessageBtn");
const adminMessage = document.getElementById("adminMessage");

if (messageToggle && messageBox) {
  messageBox.classList.add("hidden");

  messageToggle.addEventListener("click", function () {
    const isHidden = messageBox.classList.contains("hidden");
    messageBox.classList.toggle("hidden", !isHidden);
    messageBox.setAttribute("aria-hidden", String(!isHidden));

    if (isHidden && adminMessage) {
      adminMessage.focus();
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

    if (!text) {
      alert("Please write a message before sending.");
      adminMessage.focus();
      return;
    }

    alert("Message sent successfully.");
    adminMessage.value = "";
    messageBox.classList.add("hidden");
    messageBox.setAttribute("aria-hidden", "true");
  });
}
