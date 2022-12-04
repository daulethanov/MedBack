let menuBtn = document.querySelector('.menu__btn');
let navbar = document.querySelector('.navbar');

// Модальное окно
let modulBtn = document.querySelector('.btn__vhod');
let modul = document.querySelector('.modul');
let modulPosition = document.querySelector('.modul__position');
let btnClose = document.querySelector('.close');

modulBtn.addEventListener('click', function () {
	modul.classList.add('active');
	modulPosition.classList.add('active');
})

btnClose.addEventListener('click', function () {
	modul.classList.remove('active');
	modulPosition.classList.remove('active');
});

// Бургер меню
menuBtn.addEventListener('click', function () {
	menuBtn.classList.toggle('active');
	navbar.classList.toggle('active');
})

// карусель
let offset = 0;
const sliderLine = document.querySelector('.slider__line');


document.querySelector('.slider-next').addEventListener('click', function () {
	offset = offset + 1100;
	if (offset > 3300) {
		offset = 0;
	}
	sliderLine.style.left = -offset + 'px';
})

document.querySelector('.slider-prev').addEventListener('click', function () {
	offset = offset - 1100;
	if (offset < 0) {
		offset = 3300;
	}
	sliderLine.style.left = -offset + 'px';
})


// Карусель > 1200px
const sliderLineTo = document.querySelector('.slider__line-2');


document.querySelector('.slider-next-2').addEventListener('click', function () {
	offset = offset + 900;
	if (offset > 2700) {
		offset = 0;
	}
	sliderLineTo.style.left = -offset + 'px';
})

document.querySelector('.slider-prev-2').addEventListener('click', function () {
	offset = offset - 900;
	if (offset < 0) {
		offset = 2700;
	}
	sliderLineTo.style.left = -offset + 'px';
})


// Вопрос слайдер
const sliderLineAnswer = document.querySelector('.slider__line__answer');


document.querySelector('.slider-next__answer').addEventListener('click', function () {
	offset = offset + 550;
	if (offset > 1100) {
		offset = 0;
	}
	sliderLineAnswer.style.left = -offset + 'px';
})

document.querySelector('.slider-prev__answer').addEventListener('click', function () {
	offset = offset - 550;
	if (offset < 0) {
		offset = 1100;
	}
	sliderLineAnswer.style.left = -offset + 'px';
})

// Вопрос слайдер < 1200px

const sliderLineAnswerTo = document.querySelector('.slider__line__answer-2');


document.querySelector('.slider-next__answer-2').addEventListener('click', function () {
	offset = offset + 450;
	if (offset > 900) {
		offset = 0;
	}
	sliderLineAnswerTo.style.left = -offset + 'px';
})

document.querySelector('.slider-prev__answer-2').addEventListener('click', function () {
	offset = offset - 450;
	if (offset < 0) {
		offset = 900;
	}
	sliderLineAnswerTo.style.left = -offset + 'px';
})