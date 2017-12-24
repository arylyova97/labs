window.onload = function () {
    if (location.href.indexOf('services') !== -1) {
        new ServiceList(document.getElementById('list-bitch-talala'));
        new AddServicePopup();
    }
};