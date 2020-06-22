//BIG TODO: csrf

async function query_star(pk, isQuestion = false) {
	return fetch('/ajax/' + (isQuestion ? 'question' : 'answer') + '/' + pk + '/is_star', {
		method: 'GET',
		credentials: 'include'
	}).then((response) => { return response.json(); }).then((data) => { return data.star; });
}

async function mark_star(pk, star, isQuestion = false) {
	query_star(pk, isQuestion).then((data) => { star.innerHTML = data ? '&starf;' : '&star;'; });
}

stars = document.querySelectorAll(".star");
for(star of stars) {
	pk = star.id;
	mark_star(pk, star);
	star.addEventListener('click', () => {
		fetch('/ajax/answer/' + pk + '/star/', {
			method: 'POST',
			credentials: 'include'
		}).then(() => { mark_star(pk, star); });
	});
}

q_star = document.querySelector(".qstar");
if(q_star != null) {
	pk = q_star.id
	mark_star(pk, q_star, true)
	q_star.addEventListener('click', () => {
		fetch('/ajax/question/' + pk + '/star/', {
			method: 'POST',
			credentials: 'include'
		}).then(mark_star(pk, q_star, true));
	});
}

async function query_answer_c(pk) {
	return fetch('/ajax/answer/' + pk + '/is_correct', {
		method: 'GET',
		credentials: 'include'
	}).then((response) => { return response.json(); }).then((data) => { return data.correct; });
}

async function do_mark_text(pk, marker) {
	query_answer_c(pk).then((data) => { marker.innerHTML = data ? "Unmark as correct" : "Mark as correct"; });
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

