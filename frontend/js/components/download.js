export default function downloadPDF(breastCancerInfo) {
	let doc = new jsPDF();

	const source = document.getElementById("resultInfo");

	doc.fromHTML(source, 15, 15, {
		width: 170,
	});

	doc.addPage();

	const breastCancerInfoPTLabels = [
		"Número do código de amostra",
		"Espessura do Aglomerado",
		"Uniformidade do Tamanho da Célula",
		"Uniformidade da Forma da Célula",
		"Adesão Marginal",
		"Tamanho único da célula epitelial",
		"Núcleos nus",
		"Cromatina Insípida",
		"Nucléolos normais",
		"Mitoses",
	];

	doc.setFontStyle("bold");

	doc.text("INFORMAÇÕES FORNECIDAS PARA A IA", 15, 30);

	doc.setFontStyle("normal");

	let lineHeight = 45;

	breastCancerInfoPTLabels.forEach((breastCancerInfoPTLabel, index) => {
		doc.text(
			`${breastCancerInfoPTLabel}.........................................${
				Object.entries(breastCancerInfo)[index][1]
			}`,
			15,
			lineHeight
		);

		lineHeight = lineHeight + 10;
	});

	doc.save("breastCancerInformation.pdf");
}
