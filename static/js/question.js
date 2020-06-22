//BIG TODO: csrf
stars = document.querySelectorAll(".star");
for(star of stars) {
	pk = star.id;
	star.addEventListener('click', () => {
		fetch('/ajax/answer/' + pk + '/star', {
			method: 'POST',
			credentials: 'include'
		});
		fetch('/ajax/answer/' + pk + '/is_star', {
			method: 'GET',
			credentials: 'include'
		}).then(response => response.json)
		.then(data => {
			if(data.star)
				star.innerHTML = '&starf;';
			else
				star.innerHTML = '&star;';
		})
	});
}

async function query_answer_c(pk) {
	return fetch('/ajax/answer/' + pk + '/is_correct', {
		method: 'GET',
		credentials: 'include'
	}).then(function(response) { return response.json(); }).then(function(data) { return data.correct; });
}

async function do_mark_text(pk, marker) {
	query_answer_c(pk).then((data) => {
		if(data)
			marker.innerHTML = "Unmark as correct";
		else
			marker.innerHTML = "Mark as correct";
	});
}

markers = document.querySelectorAll('.mark');
for(marker of markers) {
	pk = marker.id;
	do_mark_text(pk, marker);
	marker.addEventListener('click', () => {
		fetch('/ajax/answer/' + pk + '/toggle_correct', {
			method: 'POST',
			credentials: 'include'
		}).then(do_mark_text(pk, marker));
	});
}

