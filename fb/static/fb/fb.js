/**
 * Created by Lee.Gent on 12/03/2015.
 */
function go(editor, check_endpoint_url, entry_id, entry_email)
{
    var source_text = editor.getValue();

    var molested_source_text = "(" + source_text + ")";

    var fn = null;
    var results = null;

    try {
        fn = eval(molested_source_text);
        results = fn();
    }
    catch (e) {
        $("#popup").text(e.message);
        $("#popup").dialog("open");
        return;
    }

    var results = fn();

    $.ajax({
        url: check_endpoint_url,
        method: "POST",
        data: JSON.stringify({"payload": results, "entryid": entry_id, "source": source_text})
    }).done(function(result) {
        $("#popup").html("<p style='text-align: center;'>SUCCESS</p><embed id='roll' src='/static/fb/donttouchme.swf' height='300' width='400'>");
        $("#popup").dialog("option", "close", function(evt) {
            document.location.replace("/table?mail="+entry_email);
        });

        $("#popup").dialog("open");


    }).fail(function(result) {
        $("#popup").text("Results were incorrect, sorry!");
        $("#popup").dialog("open");
    });

}

