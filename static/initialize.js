/*
 Global variables.
 (Hey, it's JS. Did you expect there wouldn't be any?
 */
var selectedSpellIDs;
var statisticsGroups;

$(function () {
    $.getJSON("/behind-the-scenes/statistics/", function (data) {
        if (data.status === 200) {
            statisticsGroups = data.content;
        }
    });

    setListeners();

    selectedSpellIDs = [];
});