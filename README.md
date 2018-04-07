# FICSv1.0
Author: Arya T Gupta

Contact: arya.tanmay.gupta@gmail.com

Programming language: Python v3

# How to access the software?
The line 14 of main.py introduces a variable "st". The string stored in this variable is processed and water height is extracted.

This software can be attached to a larger system which fetches posts in real time. The file "main.py" can be called from such a system to generate water height at various geolocations and map a flood in real time.

The variable "height" defined at line 203 of the file process.py contains the height of water that has been extracted from the string which was passed through "st" introduced at line 14 of main.py.

# About this software
This is a referral repository for a project, which has been published as an original research paper.

This is an interdisciplinary project that involves subjects like environmental engineering, artificial intelligence, and machine learning. This paper was published in the <b>Open Water Journal, Brigham Young University Press, Volume 5, Issue 2, 2018</b>.

This paper presents a software system called Fics (fetch information through crowdsourcing). Fics is a platform that is ready-to-take posts from social media platforms and infers the water heights referred in them. These posts are expected to come from the citizens who are witnessing a flood event in real time. Fics corrects the spacing in the string, translates the string into corresponding mathematical notations and then finally compute the water heights from the posts.

The objective of Fics is to provide such a platform that can be used for the citizens from the data received from them only, without making them use a software which is to be installed on their machines separately. Fics employs Artificial Intelligence to infer the required values (water heights) from the posts. Fics ignores the invalid input strings.

This software provides such an opportunity to the people that they don't need any specific format, any specific platform to give the real-time information about an ongoing flood event. They just need to use their phones or any system that is available and post their status publicly through social media. The server in which this system is installed will convert their posts to extract required mathematical information about the information of the geographical location which is tagged with the post, for example, the water height. In this way,

   -	scientific modelling of the flood can be done in real time. This will help in forecasting the immediate nature of the flood and its extent according to the terrain of the locality; also the nature and probability of future floods. 
   -	immediate help can be provided to the citizens who are trapped because of a natural calamity or a major accident which is man-made, a flood in this case.

There were works already available who focus on gathering such data. Those works are cited in the paper. All of these projects need a form to be filled through which required information and values are to be submitted. On this other hand, Fics provides platform independence to the citizens and no extra application needs to be installed.

Link to paper: https://scholarsarchive.byu.edu/openwater/vol5/iss2/2
