---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
permalink: /index.html
header:
  image_fullwidth: software-carpentry-banner.png
widget1:
  title: 'Our Workshops'
  url: '/workshops/'
  text: 'Host a workshop or find one to attend.'
  image: workshops/2012-12-uta.png
widget2:
  title: 'Our Lessons'
  url: '/lessons/'
  text: 'Have a look at what we teach.'
  image: workshops/dc-2014.jpg
widget3:
  title: 'Get Involved'
  url: '/join/'
  text: 'Help teach or join the discussion.'
  image: workshops/scripps-2012-11.png
---
<div class="row">
  <div class="small-2 columns">
    <img src="{{site.filesurl}}/orgs/data-carpentry.png" alt="Data Carpentry" />
  </div>
  <div class="small-10 columns">
    <p>
      You may also want to check out our sibling project
      <a href="http://datacarpentry.org">Data Carpentry</a>
      which develops and teaches workshops on the fundamental data skills.
    </p>
  </div>
</div>
