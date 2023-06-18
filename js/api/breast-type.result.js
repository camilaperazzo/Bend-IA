export default async function verifyBreastType(breastInfo) {
	const body = JSON.stringify(breastInfo);
	console.log(body);

	return fetch("http://localhost:5500/js/api/breast-type-result.json")
		.then(response => response.json())
		.catch(error => console.warn(error));
}
