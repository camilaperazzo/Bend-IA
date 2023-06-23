export default async function verifyBreastCancerType(breastCancerInfo) {
	const options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(breastCancerInfo),
	};

	return fetch("http://localhost:5000/predict", options)
		.then(response => response.json())
		.catch(error => console.warn(error));
}
