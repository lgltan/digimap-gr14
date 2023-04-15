const imageInput = document.getElementById("imageInput");
const pwInput1 = document.getElementById("pw-input-1");
const pwInput2 = document.getElementById("pw-input-2");
const uploadBtn = document.getElementById("uploadBtn");
const imageContainer = document.getElementById("imageContainer");
const icon = document.getElementById("toggle-icon");
const title = document.getElementById("mode-text");

uploadBtn.addEventListener("click", () => {
	const file = imageInput.files[0];
	if (file) {
		const reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onload = () => {
			const img = document.createElement("img");
			img.src = reader.result;
			imageContainer.innerHTML = "";
			imageContainer.appendChild(img);
		};
		imageContainer.style.display = "flex";
		imageInput.style.display = "none";
		pwInput1.style.display = "none";
		pwInput2.style.display = "none";
		uploadBtn.innerHTML = "Download";
	}
});

// icon toggle
let images = ["icons/lock.png", "icons/unlock.png"];
let mode = ["Image Encryption", "Image Decryption"];
let color_arr = ["#2a8c2b", "#8c2d2a"];
let btnText = ["Encrypt", "Decrypt"];
let index = 0;
function toggleIcon() {
    index = (index + 1) % 2;
    icon.setAttribute("src", images[index]);
    title.innerHTML = mode[index];
    title.style.color = color_arr[index];
	uploadBtn.innerHTML = btnText[index];
}
icon.addEventListener("click", toggleIcon);