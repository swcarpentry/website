<table class="table table-striped workshops"  style="width: 100%;">
  {% for w in workshop_list %}
  <tr>
<td>
  <img src="{{site.filesurl}}/flags/{{site.flag_size}}/{{w.country | downcase}}.png" title="{{w.country | replace: '-', ' '}}" alt="{{w.country | replace: '-', ' ' | downcase}}" />
  <a href="{{w.url}}">{{w.venue}}</a>
      <br/>
  {{w.start_date | date: "%b %-d"}} - {{w.end_date | date: "%b %-d, %Y"}}
      {% if w.instructors %}
      <br/>
      <b>Instructors:</b> {{ w.instructors | replace: ",", ", "}}
      {% endif %}
      {% if w.helpers %}
      <br/>
      <b>Helpers:</b> {{ w.helpers  | replace: ",", ", "}}
      {% endif %}
</td>
  </tr>
  {% endfor %}

</table>
