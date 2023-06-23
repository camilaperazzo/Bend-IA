import verifyBreastCancerType from "./api/breast-cancer-type.result.js";
import { closeModal, createResult, openModal } from "./components/modal.js";

const form = document.querySelector(".form");
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
	openModal();

	let breastCancerInfo = {};

	FIELD_NAMES.forEach(cur_infoName => {
		breastCancerInfo[`${cur_infoName}`] = parseInt(
			document.getElementsByName(`${cur_infoName}`)[0].value
		);
	});

	verifyBreastCancerType(breastCancerInfo)
		.then(response => createResult(breastCancerInfo, response))
		.catch(error => {
			closeModal();
			alert("Invalid Data, please, look at your responses and try again");
			console.error(error);
		});
});
