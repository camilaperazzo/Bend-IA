import verifyBreastCancerType from "./api/breast-cancer-type.result.js";
import initModal from "./components/modal.js";

const form = document.querySelector(".form");
const modal = document.querySelector(".modal");

form.addEventListener("submit", async e => {
	e.preventDefault();
	modal.classList.add("active");

	const breastCancerInfo = {
		sampleCodeNumber:
			document.getElementsByName("sample-code-number")[0].value,
		agglomerateThickness: document.getElementsByName(
			"agglomerate-thickness"
		)[0].value,
		cellSizeUniformity: document.getElementsByName(
			"cell-size-uniformity"
		)[0].value,
		cellShapeUniformity: document.getElementsByName(
			"cell-shape-uniformity"
		)[0].value,
		marginalAdherence:
			document.getElementsByName("marginal-adherence")[0].value,
		oneSizeEpithelialCell: document.getElementsByName(
			"one-size-epithelial-cell"
		)[0].value,
		nakedCores: document.getElementsByName("naked-cores")[0].value,
		chromatin: document.getElementsByName("chromatin")[0].value,
		normalNucleoli: document.getElementsByName("normal-nucleoli")[0].value,
		mitosis: document.getElementsByName("mitosis")[0].value,
	};

	const breastCancerResult = await verifyBreastCancerType(breastCancerInfo);

	if (breastCancerResult) {
		window.setTimeout(
			() => initModal(breastCancerInfo, breastCancerResult),
			100 * 6
		);
	}
});
