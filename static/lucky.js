/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
	evt.preventDefault();

	let name = $("#name").val();
	let year = $("#year").val();
	let email = $("#email").val();
	let color = $("#color").val();

	resp = await axios.post("http://127.0.0.1:5000/api/get-lucky-num", {
		name,
		year,
		email,
		color,
	});

	handleResponse(resp);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
	let numResp = resp.data.num;
	let yearResp = resp.data.year;

	$("#lucky-results").append(`
    <p>Your lucky number is ${numResp.num} (${numResp.fact}).</p>
    <p>Your birth year (${yearResp.year}) fact is ${yearResp.fact}.</p>
    `);
}

$("#lucky-form").on("submit", processForm);
