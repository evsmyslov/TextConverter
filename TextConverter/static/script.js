async function convertText(mode) {
  const text = document.getElementById("inputText").value;
  const formData = new FormData();
  formData.append("text", text);
  formData.append("mode", mode);

  const response = await fetch("/convert", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  document.getElementById("outputText").value = data.result;
}

function copyToClipboard() {
  const output = document.getElementById("outputText");
  output.select();
  document.execCommand("copy");
}

function toggleTheme() {
  const body = document.body;
  const button = document.getElementById("themeToggle");
  const isDark = body.classList.toggle("dark-theme");
  body.classList.toggle("light-theme", !isDark);
  button.textContent = isDark ? "☀️" : "🌙";
}

