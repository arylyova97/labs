/*
 <div class="card col-sm-3">
                <img class="card-img-top" src= "/{{service.image}}"  alt="Card image cap">
                <div class="card-body">
                    <p class="card-title">{{ service.title }}</p>
                    <p class="card-text">{{ service.company }}</p>
                </div>
                <div class="card-body">
                    <a class="btn btn-info" role="button" href="{% url 'service' service.id %}">More</a>
                </div>
            </div>*/

function ServiceList(node) {
    this.node = node;
    this.limit = 6;
    this.offset = 0;
    this.canLoadMore = true;
    this._init();
}

ServiceList.prototype.incrementOffset = function () {
    this.offset += this.limit;
};

ServiceList.prototype._init = function () {
    this.getServices();
    this.initScrollListener();
};

ServiceList.prototype.getServices = function () {
    var _this = this;
    request('/get-services/' + '?limit=' + this.limit + '&offset=' + this.offset, 'GET').then(function (res) {
        if (res.status !== 200) {
            return;
        }
        _this.createCards(res.json);
    }).catch(function (err) {
        console.error(err);
    });
};

ServiceList.prototype.createCards = function (data) {
    if (data.length === 0) {
        this.canLoadMore = false;
        return;
    }
    var _this = this;
    data.forEach(function (elData) {
        var card = _this.createCard(elData);
        _this.node.appendChild(card);
    });
};

ServiceList.prototype.createCard = function (data) {
    var mainContainer = createElement('div', {
        class: 'card col-sm-3'
    });
    var img = createElement('img', {
        class: 'card-img-top',
        src: '/' + data.img
    });
    var cardBody = createElement('div', {
        class: 'card-body'
    });
    var title = createElement('p', {
        class: 'card-title'
    }, data.title);
    var company = createElement('p', {
        class: 'card-text'
    }, data.company);
    cardBody.appendChild(title);
    cardBody.appendChild(company);

    var hrefContainer = createElement('div', {
        class: 'card-body'
    });
    var a = createElement('a', {
        class: 'btn btn-info',
        role: 'button',
        href: '/service/' + data.id
    }, 'More');
    hrefContainer.appendChild(a);

    mainContainer.appendChild(img);
    mainContainer.appendChild(cardBody);
    mainContainer.appendChild(hrefContainer);
    return mainContainer;
};

ServiceList.prototype.initScrollListener = function () {
    var _this = this;
    window.onscroll = function () {
        var el = document.documentElement;
        if (el.scrollTop === el.scrollHeight - el.clientHeight && _this.canLoadMore) {
            _this.incrementOffset();
            _this.getServices();
        }
    }
};