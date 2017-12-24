function AddServicePopup() {
    this.title = document.getElementById('add-title');
    this.imageFile = document.getElementById('add-image');
    this.imgPrev = document.getElementById('add-img-prev');
    this.addSubmit = document.getElementById('add-submit');
    this.addModal = document.getElementById('AddModal');
    this.imgPrev.classList.add('hidden');
    this.init();
}

AddServicePopup.prototype.init = function () {
    this.setListenersImg();
    this.setSubmitListener();
};

AddServicePopup.prototype.setSubmitListener = function () {
    var _this = this;
    this.addSubmit.addEventListener('click', function (e) {
        request('/add-service/', 'POST', {
            img: _this.imgResultData,
            title: _this.title.value,
            category: _this.category,
            company: _this.company,
            price: _this.price,
            short_info: _this.short_info
        }).then(function (res) {
            console.warn(res);
            _this.addModal.style.removeProperty('display');
        }).catch(function (err) {
            alert(err);
        });
    });
};

AddServicePopup.prototype.setListenersImg = function () {
    var _this = this;
    this.imageFile.onchange = function (el) {
        var target = el.currentTarget;
        if (target.files && target.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                _this.imgPrev.setAttribute('src', e.target.result);
                _this.imgResultData = e.target.result;
                _this.imgPrev.classList.remove('hidden');
            };

            reader.readAsDataURL(target.files[0]);
        }
    }
};