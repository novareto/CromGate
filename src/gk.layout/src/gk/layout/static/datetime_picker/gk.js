$(document).ready(function() {

    function add_datepicker(inputid) {
	var field = $(inputid).parent('.field');
	field.addClass('input-append');
	field.append('<span class="add-on"><i data-time-icon="icon-time" data-date-icon="icon-calendar"></i></span>');

	field.datetimepicker({
        format: 'DD.MM.YYYY HH:mm:SS',
            language: 'de'
	});
    }

    add_datepicker('#form-field-disable');
    add_datepicker('#form-field-enable');

})
