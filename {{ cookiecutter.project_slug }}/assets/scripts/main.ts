const btn = document.querySelector<HTMLButtonElement>("#alert-btn");

if (btn) {
  btn.addEventListener("click", () => {
    alert("AHHHH!!");
  });
}
