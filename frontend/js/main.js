import verifyBreastCancerType from "./api/breast-cancer-type.result.js";
import initModal from "./components/modal.js";

const form = document.querySelector(".form");
const modal = document.querySelector(".modal");

const FIELD_NAMES = [
	"sampleCodeNumber",
	"agglomerateThickness",
	"cellSizeUniformity",
	"cellShapeUniformity",
	"marginalAdherence",
	"oneSizeEpithelialCell",
	"nakedCores",
	"chromatin",
	"normalNucleoli",
	"mitosis",
];

form.addEventListener("submit", async e => {
	e.preventDefault();
	modal.classList.add("active");

	let breastCancerInfo = {};

	FIELD_NAMES.forEach(cur_infoName => {
		breastCancerInfo[`${cur_infoName}`] = parseInt(
			document.getElementsByName(`${cur_infoName}`)[0].value
		);
	});

	const breastCancerResult = await verifyBreastCancerType(breastCancerInfo);

	initModal(breastCancerInfo, breastCancerResult);
});
