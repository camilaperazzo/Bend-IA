import downloadPDF from "./download.js";

function closeModal() {
	const modal = document.querySelector(".modal");
	const result = document.querySelector(".result");

	if (result) {
		result.remove();
		modal.querySelector(".loading").style.display = "block";
	}

	modal.classList.remove("active");
}

function createResult(breastCancerInfo, { sampleCode, result, hitPercentage }) {
	const modal = document.querySelector(".modal");

	const resultHTMLStructure = `
            <div class="top-section">
                <div class="close-button-container">
                    <button class="close-button">
                        <img src="./img/close.svg" alt="close button" />
                    </button>
                </div>

                <div class="result-info-container">
                    <div class="result-info" id="resultInfo">
                        <h1>Resultado - Amostra <b>${sampleCode}</b></h1>
                        <p>
                            Após análise há uma chance de
                            <b>${hitPercentage}%</b> do câncer ser
                            <b>${result}</b>
                        </p>
                        <p>
                            A única forma concreta de confirmar se um tumor é
                            benigno ou maligno é procurando a ajuda de um médico
                            especialista. O médico irá fazer um levantamento do
                            histórico médico do paciente, um exame físico e
                            ainda solicitar exames complementares para a
                            confirmação do tipo de tumor.
                        </p>
                    </div>

                    <button class="download-button">
                        <img
                            src="./img/download.svg"
                            alt="download button"
                            width="40px"
                            height="40px"
                        />
                    </button>
                </div>
            </div>

            <button class="button">Concluir</button>
    `;

	let resultElement = document.createElement("div");
	resultElement.classList.add("result");
	resultElement.innerHTML = resultHTMLStructure;

	modal.querySelector(".loading").style.display = "none";
	modal.appendChild(resultElement);

	document
		.querySelector(".result .button")
		.addEventListener("click", closeModal);

	if (window.screen.width >= 768) {
		document
			.querySelector(".result .close-button")
			.addEventListener("click", closeModal);
	}

	document
		.querySelector(".result .download-button")
		.addEventListener("click", () => downloadPDF(breastCancerInfo));
}

function openModal() {
	document.querySelector(".modal").classList.add("active");
}

export { closeModal, createResult, openModal };
