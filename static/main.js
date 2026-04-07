const uploadForm = document.getElementById("upload-form");
const imageInput = document.getElementById("image-input");
const fileName = document.getElementById("file-name");
const previewWrapper = document.getElementById("preview-wrapper");
const imagePreview = document.getElementById("image-preview");

const loadingBox = document.getElementById("loading");
const resultBox = document.getElementById("result");
const errorBox = document.getElementById("error-message");

const resultFinal = document.getElementById("result-final");
const resultBinaryClass = document.getElementById("result-binary-class");
const resultBinaryConfidence = document.getElementById("result-binary-confidence");
const resultBinaryRaw = document.getElementById("result-binary-raw");

const situationBox = document.getElementById("situation-box");
const resultSituationClass = document.getElementById("result-situation-class");
const resultSituationConfidence = document.getElementById("result-situation-confidence");

imageInput.addEventListener("change", () => {
    resultBox.classList.add("hidden");
    errorBox.classList.add("hidden");

    if (imageInput.files.length === 0) {
        fileName.textContent = "Zatím není vybraný žádný soubor.";
        previewWrapper.classList.add("hidden");
        imagePreview.src = "";
        return;
    }

    const selectedFile = imageInput.files[0];
    fileName.textContent = `Vybraný soubor: ${selectedFile.name}`;

    if (selectedFile.type.startsWith("image/")) {
        const objectUrl = URL.createObjectURL(selectedFile);
        imagePreview.src = objectUrl;
        previewWrapper.classList.remove("hidden");
    } else {
        previewWrapper.classList.add("hidden");
        imagePreview.src = "";
    }
});

uploadForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (imageInput.files.length === 0) {
        showError("Nejdřív vyber obrázek.");
        return;
    }

    const submitButton = uploadForm.querySelector("button[type='submit']");
    submitButton.disabled = true;

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    loadingBox.classList.remove("hidden");
    resultBox.classList.add("hidden");
    errorBox.classList.add("hidden");
    situationBox.classList.add("hidden");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || "Nepodařilo se zpracovat obrázek.");
            return;
        }

        resultFinal.textContent = data.final_class_name;
        resultBinaryClass.textContent = data.binary_class_name;
        resultBinaryConfidence.textContent = data.binary_confidence_percent;
        resultBinaryRaw.textContent = data.binary_raw_output;

        if (data.situation_class_name) {
            resultSituationClass.textContent = data.situation_class_name;
            resultSituationConfidence.textContent = data.situation_confidence_percent;
            situationBox.classList.remove("hidden");
        } else {
            situationBox.classList.add("hidden");
        }

        resultBox.classList.remove("hidden");
    } catch (error) {
        showError("Chyba při komunikaci se serverem.");
    } finally {
        loadingBox.classList.add("hidden");
        submitButton.disabled = false;
    }
});

function showError(message) {
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
}