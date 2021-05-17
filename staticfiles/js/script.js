$(document).ready(function() {
	
	
	$('.pointer').parent().siblings('ul').hide();

	$('i').on('click',function(){
		$(this).parent().parent().next('ul').show();
	});

	$('.img-fit').on('click',function(){
		$('.img-fit').attr("style","opacity:0.3 !important");
		$(this).attr("style","opacity:1 !important");
		if($(this).attr('alt')=='OSF'){
			$('.selected-service').val('OSF');
			$('.provider-name').text('OSF Preprints');
			$('.provider-desc').text('A scholarly commons to connect the entire research cycle');
		};


		if($(this).attr('alt')=='AfricArXiv'){
			$('.selected-service').val('AfricArXiv');
			$('.provider-name').text('AfricArXiv');
			$('.provider-desc').text('A free preprint service for African scientists');
		};

		if($(this).attr('alt')=='BioHackrXiv'){
			$('.selected-service').val('BioHackrXiv');
			$('.provider-name').text('BioHackrXiv');
			$('.provider-desc').text('Preprints for BioHackathons');
		};

		if($(this).attr('alt')=='BodoArXiv'){
			$('.selected-service').val('BodoArXiv');
			$('.provider-name').text('BodoArXiv');
			$('.provider-desc').text('Open Repository for Medieval Studies Visit BodoArXiv.org to learn more.');
		};

		if($(this).attr('alt')=='EcoEvoRxiv'){
			$('.selected-service').val('EcoEvoRxiv');
			$('.provider-name').text('EcoEvoRxiv');
			$('.provider-desc').text('A free preprint service for ecology, evolution and conservation. Visit ecoevorxiv.com for more information.');
		};

		if($(this).attr('alt')=='ECSarXiv'){
			$('.selected-service').val('ECSarXiv');
			$('.provider-name').text('ECSarXiv');
			$('.provider-desc').text('a free preprint service for electrochemistry and solid state science and technology');
		};

		if($(this).attr('alt')=='EdArXiv'){
			$('.selected-service').val('EdArXiv');
			$('.provider-name').text('EdArXiv');
			$('.provider-desc').text('A Preprint Server For The Education Research Community');


		};

		if($(this).attr('alt')=='engrXiv'){
			$('.selected-service').val('engrXiv');
			$('.provider-name').text('engrXiv');
			$('.provider-desc').text('The open archive of engineering');

		};

		if($(this).attr('alt')=='FocUS'){
			$('.selected-service').val('FocUS');
			$('.provider-name').text('FocUS Archive');
			$('.provider-desc').text('A free preprint service for the focused ultrasound research community.');

			
		};

		if($(this).attr('alt')=='MediArXiv'){
			$('.selected-service').val('MediArXiv');
			$('.provider-name').text('MediArXiv');
			$('.provider-desc').text('Open Archive for Media, Film, and Communication Studies. Visit mediarxiv.com for more information.');

			
		};


		if($(this).attr('alt')=='MetaArXiv'){
			$('.selected-service').val('MetaArXiv');
			$('.provider-name').text('MetaArXiv');
			$('.provider-desc').text('An interdisciplinary archive of articles focused on improving research transparency and reproducibility Maintained by The Berkeley Initiative for Transparency in the Social Sciences (BITSS)If you are interested in community peer-review, submit your MetaArXiv preprints to PCI Meta-Research');

		};


		if($(this).attr('alt')=='MindRxiv'){
			$('.selected-service').val('MindRxiv');
			$('.provider-name').text('MindRxiv');
			$('.provider-desc').text('Open archive for research on mind and contemplative practices');

			
		};


		if($(this).attr('alt')=='PaleorXiv'){
			$('.selected-service').val('PaleorXiv');
			$('.provider-name').text('PaleorXiv');
			$('.provider-desc').text('A preprint archive for Paleontology');

			
		};

		if($(this).attr('alt')=='PsyArXiv'){
			$('.selected-service').val('PsyArXiv');
			$('.provider-name').text('PPsyArXiv');
			$('.provider-desc').text('A free preprint service for the psychological sciences Maintained by The Society for the Improvement of Psychological Science');

			
		};




		if($(this).attr('alt')=='SocArXiv'){
			$('.selected-service').val('SocArXiv');
			$('.provider-name').text('SocArXiv');
			$('.provider-desc').text('Open archive of the social sciencesSocArXiv papers are moderated before appearing. Visit SocOpen.org for more information.');
		};



		if($(this).attr('alt')=='SportRxiv'){
			$('.selected-service').val('SportRxiv');
			$('.provider-name').text('SportRxiv');
			$('.provider-desc').text('The open access subject repository for Sport, Exercise, Performance, and Health research.SportrXiv is managed by Society for Transparency Openness and Replication in Kinesiology (STORK), for information on how to support visit, storkinesiology.org');

			
		};



		if($(this).attr('alt')=='Thesis'){
			$('.selected-service').val('Thesis');
			$('.provider-name').text('Thesis Commons');
			$('.provider-desc').text('An open archive of Theses');
		};




	});

	$("input[name='publicdata']").on('click',function(){
	var get_radio_value = $("input[name='publicdata']:checked").val();
	$('.available-data-link').css('display','none');
	$('.not-available-describe').css('display','none');
	$('.not-applicable-text').css('display','none');

	if (get_radio_value == 'available'){
		
		$('.available-data-link').attr("style","display:block !important");
	};

	if (get_radio_value == 'no'){
		$('.not-available-describe').attr('style','display:block !important');
	};


	if (get_radio_value == 'not-applicable'){
		$('.not-applicable-text').attr('style','display:block !important;background-color: #ebe6e6;padding-left: 1rem;padding-right: 1rem');
	}

})


//type form section of preregistration 



	$("input[name='type-data']").on('click',function(){
	var get_radio_value = $("input[name='type-data']:checked").val();
	$('.available-type-link').css('display','none');
	$('.main-type').css('display','none');
	$('.not-available-type-describe').css('display','none');
	$('.not-applicable-type-text').css('display','none');

	if (get_radio_value == 'type-available'){
		
		$('.available-type-link').attr("style","display:block !important");
		$('.main-type').attr("style","display:block !important");
	};

	if (get_radio_value == 'type-no'){
		$('.not-available-type-describe').attr('style','display:block !important');
	};


	if (get_radio_value == 'type-not-applicable'){
		$('.not-applicable-type-text').attr('style','display:block !important;background-color: #ebe6e6;padding-left: 1rem;padding-right: 1rem');
	};



});



	$('#license-type').change(function(){
		
		if($(this).val()=='no-license'){
			$('.year-box, .copyright-box').attr('style','display:block !important');
		}else{
			$('.year-box, .copyright-box').attr('style','display:none !important');
		}


	});




	// Section of selecting taxonomies

	$('.texonomies > li').on('click',function(){
		$('.cat-list:first > li').css('background-color','');
		$(this).css('background-color','#b8bfba');
		$("[name='selected-main-taxonomy']").val($(this).text());
		

		$('.Architecture,.artshumanities,.business,.education,.engineering,.law,.lifescience,.madicineandhealth,.physicalscienceandmath,.socialbehavioralscience').attr('style','display:none !important');

		if($(this).text()=='Architecture'){
			
			$('.Architecture').attr('style','display:block !important');
		};


		if($(this).attr('id')=='artsandhumanity'){
			
			$('.artshumanities').attr('style','display:block !important');
		};

		if($(this).text()=='Business'){
			$('.business').attr('style','display:block !important');
		};

		if($(this).text()=='Education'){
			$('.education').attr('style','display:block !important');
		};

		if($(this).text()=='Engineering'){
			$('.engineering').attr('style','display:block !important');
		};


		if($(this).text()=='Law'){
			$('.law').attr('style','display:block !important');
		};

		if($(this).text()=='Life Sciences'){
			$('.lifescience').attr('style','display:block !important');
		};

		if($(this).text()=='Medicine and Health Sciences'){
			$('.madicineandhealth').attr('style','display:block !important');
		};

		if($(this).text()=='Physical Sciences and Mathematics'){
			
			$('.physicalscienceandmath').attr('style','display:block !important');
		};

		if($(this).text()=='Social and Behavioral Sciences'){
			$('.socialbehavioralscience').attr('style','display:block !important');
		};









	})



	//end of section taxonomies


		//start of subtexonomy



		$('.sub-texonomy > li').on('click',function(){
				$('.sub-texonomy> li').css('background-color','');
				$('.selected-item').attr('style','display:block !important');
				$('.selected-item').text($(this).text());

				$('#selected-texonomy').val($(this).text());
				$(this).css('background-color','#b8bfba');

		})

		//end of sub texonomy


		//conflict of interest section 

		$("[name='conflict-interest']").on('click',function(){
			var get_radio_value = $("input[name='conflict-interest']:checked").val();
			$('.conflict-interest-describe').attr('style','display:none !important');

			$('.no-interest-text').attr('style','display:none !important');

			if(get_radio_value=='yes'){
				$('.conflict-interest-describe').attr('style','display:block !important');
			};

			if (get_radio_value=='no'){
				$('.no-interest-text').attr('style','display:block !important;background-color:#b8bfba !important;padding-left:2rem')
			}
		});

		//end of conflict of interest section


		$("input[type='checkbox']").on('click',function(event){
			if ($(this).attr('name')=='terms'){

			
			} else {
			var keyword = $(this).parent().text().trim();
	
			window.location='/preprints/search_by_topic/'+keyword;}
		});


		$(".pre-item").on('click',function(){
			var keyword = $(this).text().trim();
	
			window.location='/preprints/search_by_topic/'+keyword;
		});




})




$(document).ready(function(){

if($('.brands_slider').length)
{
var brandsSlider = $('.brands_slider');

brandsSlider.owlCarousel(
{
loop:true,
autoplay:false,
autoplayTimeout:5000,
nav:false,
dots:true,
autoWidth:true,
items:8,
margin:42
});

if($('.brands_prev').length)
{
var prev = $('.brands_prev');
prev.on('click', function()
{
brandsSlider.trigger('prev.owl.carousel');
});
}

if($('.brands_next').length)
{
var next = $('.brands_next');
next.on('click', function()
{
brandsSlider.trigger('next.owl.carousel');
});
}
}


});