export default async function verifyBreastCancerType(breastCancerInfo) {
	const body = JSON.stringify(breastCancerInfo);

	return fetch("http://localhost:5500/js/api/breast-cancer-type-result.json")
		.then(response => response.json())
		.catch(error => console.warn(error));
}
