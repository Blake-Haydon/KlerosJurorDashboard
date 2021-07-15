import {getUrlParameter} from './getUrlParameter.js'

$(function(){
    var network = getUrlParameter('network')
    console.log('Loading court table, please wait')
    $.ajax({
        url: '/_getRetention',
        data: {"network": network},
        type: 'GET',
        success: function(response, network){
            console.log(response)
            $('#retentionValue').html('<h4>'+parseFloat(response*100).toFixed(2)+'%</h4>');
        },
        error: function(error){
            console.log(error);
            $('#retentionValue').html('Eror loading adoption');
        }
    });
});
