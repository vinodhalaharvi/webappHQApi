htmlmap = {
  'user_create':   r'''<div class="form" align="center">
  <form id="target" action="false" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden"/>
      <input type="hidden" name="actionName" value="user_create" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name*">name*:</label>
      <input type="text" name="name" id="name" />
      <br />
      <label for="firstName*">firstName*:</label>
      <input type="text" name="firstName" id="firstName" />
      <br />
      <label for="lastName*">lastName*:</label>
      <input type="text" name="lastName" id="lastName" />
      <br />
      <label for="phoneNumber">phoneNumber:</label>
      <input type="text" name="phoneNumber" id="phoneNumber" />
      <br />
      <label for="department">department:</label>
      <input type="text" name="department" id="department" />
      <br />
      <label for="SMSAddress">SMSAddress:</label>
      <input type="text" name="SMSAddress" id="SMSAddress" />
      <br />
      <label for="htmlEmail">htmlEmail:</label>
      <input type="text" name="htmlEmail" id="htmlEmail" />
      <br />
      <label for="active">active:</label>
      <input type="text" name="active" id="active" />
      <br />
      <label for="emailAddress*">emailAddress*:</label>
      <input type="text" name="emailAddress" id="emailAddress" />
      <br />
      <label for="password*">password*:</label>
      <input type="password" name="password" id="password" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>  
   </form>
</div>''', 
  'user_changePassword': r'''<div class="form" align="center">
  <form id="target" action="false" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden"/>
      <input type="hidden" name="actionName" value="user_changePassword" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="password*">password*:</label>
      <input type="password" name="password" id="password" />
      <br />
      <label for="name*">name*:</label>
      <input type="text" name="name" id="name" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>''',
  'user_delete':   r'''<div class="form" align="center">
  <form id="target" action="false" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden"/>
      <input type="hidden" name="actionName" value="user_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name*">name*:</label>
      <input type="text" name="name*" id="name*" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>''',
  'user_sync': r'''<div class="form" align="center">
  <form id="target" action="false" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden"/>
      <input type="hidden" name="actionName" value="user_sync" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="xml_to_sync*">xml_to_sync*:</label>
      <textarea cols="100" rows="30" name="xml_to_sync" id="xml_to_sync">$data</textarea>
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>''',
'resource_getResourcePrototypes':r''' <div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_getResourcePrototypes" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="existing">existing:</label>
      <input type="text" name="existing" id="existing" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>''',
'resource_getResourcePrototype':r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_getResourcePrototype" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name">name*:</label>
      <input type="text" name="name" id="name" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>''',
'resource_get': r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="children">children:</label>
      <input type="text" name="children" id="children" />
      <br></br>
      <label for="platformName">platformName:</label>
      <input type="text" name="platformName" id="platformName" />
      <br></br>
      <label for="id">id:</label>
      <input type="text" name="id" id="id" />
      <br></br>
      <label for="verbose">verbose:</label>
      <input type="text" name="verbose" id="verbose" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>''',
'resource_find': r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_find" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="prototype">prototype:</label>
      <input type="text" name="prototype" id="prototype" />
      <br></br>
      <label for="agentId">agentId:</label>
      <input type="text" name="agentId" id="agentId" />
      <br></br>
      <label for="children">children:</label>
      <input type="text" name="children" id="children" />
      <br></br>
      <label for="description">description:</label>
      <input type="text" name="description" id="description" />
      <br></br>
      <label for="verbose">verbose:</label>
      <input type="text" name="verbose" id="verbose" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
  </div>''',
  'resource_sync': r'''<div class="form" align="center">
  <form id="target" action="false" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden"/>
      <input type="hidden" name="actionName" value="resource_sync" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="xml_to_sync*">xml_to_sync*:</label>
      <textarea style="width: 50%; height: 50%;" name="xml_to_sync" id="xml_to_sync">$data</textarea>
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>''',
'resource_delete': r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>''',
'resource_move': r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_move" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="destinationId">destinationId*:</label>
      <input type="text" name="destinationId" id="destinationId" />
      <br></br>
      <label for="targetId">targetId*:</label>
      <input type="text" name="targetId" id="targetId" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>''', 'alertdefinition_listDefinitions': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alertdefinition_listDefinitions" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="excludeTypeBased">excludeTypeBased:</label>
      <input type="text" name="excludeTypeBased" id="excludeTypeBased" />
      <br></br>
      <label for="escalationId">escalationId:</label>
      <input type="text" name="escalationId" id="escalationId" />
      <br></br>
      <label for="groupName">groupName:</label>
      <input type="text" name="groupName" id="groupName" />
      <br></br>
      <label for="resourceId">resourceId:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br></br>
      <label for="resourceNameFilter">resourceNameFilter:</label>
      <input type="text" name="resourceNameFilter" id="resourceNameFilter" />
      <br></br>
      <label for="alertNameFilter">alertNameFilter:</label>
      <input type="text" name="alertNameFilter" id="alertNameFilter" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>
''', 'alertdefinition_listTypeDefinitions': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alertdefinition_listTypeDefinitions" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="excludeIds">excludeIds:</label>
      <input type="text" name="excludeIds" id="excludeIds" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>
''', 'alertdefinition_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alertdefinition_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br></br>
      <input type="submit" name="submit" id="submit" />
      <br></br>
    </fieldset>
  </form>
</div>
'''
, 'resource_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="children">children:</label>
      <input type="text" name="children" id="children" />
      <br />
      <label for="platformName">platformName:</label>
      <input type="text" name="platformName" id="platformName" />
      <br />
      <label for="id">id:</label>
      <input type="text" name="id" id="id" />
      <br />
      <label for="verbose">verbose:</label>
      <input type="text" name="verbose" id="verbose" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'resource_find': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_find" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="prototype">prototype:</label>
      <input type="text" name="prototype" id="prototype" />
      <br />
      <label for="agentId">agentId:</label>
      <input type="text" name="agentId" id="agentId" />
      <br />
      <label for="children">children:</label>
      <input type="text" name="children" id="children" />
      <br />
      <label for="description">description:</label>
      <input type="text" name="description" id="description" />
      <br />
      <label for="verbose">verbose:</label>
      <input type="text" name="verbose" id="verbose" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'resource_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'resource_move': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="resource_move" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="destinationId">destinationId*:</label>
      <input type="text" name="destinationId" id="destinationId" />
      <br />
      <label for="targetId">targetId*:</label>
      <input type="text" name="targetId" id="targetId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alertdefinition_listDefinitions': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alertdefinition_listDefinitions" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="excludeTypeBased">excludeTypeBased:</label>
      <input type="text" name="excludeTypeBased" id="excludeTypeBased" />
      <br />
      <label for="escalationId">escalationId:</label>
      <input type="text" name="escalationId" id="escalationId" />
      <br />
      <label for="groupName">groupName:</label>
      <input type="text" name="groupName" id="groupName" />
      <br />
      <label for="resourceId">resourceId:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <label for="resourceNameFilter">resourceNameFilter:</label>
      <input type="text" name="resourceNameFilter" id="resourceNameFilter" />
      <br />
      <label for="alertNameFilter">alertNameFilter:</label>
      <input type="text" name="alertNameFilter" id="alertNameFilter" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alertdefinition_listTypeDefinitions': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alertdefinition_listTypeDefinitions" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="excludeIds">excludeIds:</label>
      <input type="text" name="excludeIds" id="excludeIds" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
,'metric_getTemplates': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getTemplates" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="prototype">prototype*:</label>
      <input type="text" name="prototype" id="prototype" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getMetricTemplate': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getMetricTemplate" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getMetrics': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getMetrics" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <label for="enabled">enabled:</label>
      <input type="text" name="enabled" id="enabled" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getMetric': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getMetric" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getData': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getData" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="metricId">metricId*:</label>
      <input type="text" name="metricId" id="metricId" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getGroupData': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getGroupData" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="groupId">groupId*:</label>
      <input type="text" name="groupId" id="groupId" />
      <br />
      <label for="templateId">templateId*:</label>
      <input type="text" name="templateId" id="templateId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metric_getResourceData': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metric_getResourceData" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="ids">ids*:</label>
      <input type="text" name="ids" id="ids" />
      <br />
      <label for="templateId">templateId*:</label>
      <input type="text" name="templateId" id="templateId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'agent_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="agent_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'agent_ping': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="agent_ping" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'autodiscovery_approve': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="autodiscovery_approve" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'maintenance_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="maintenance_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="groupId">groupId*:</label>
      <input type="text" name="groupId" id="groupId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'maintenance_schedule': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="maintenance_schedule" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="groupId">groupId*:</label>
      <input type="text" name="groupId" id="groupId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'maintenance_unschedule': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="maintenance_unschedule" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="groupId">groupId*:</label>
      <input type="text" name="groupId" id="groupId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'escalation_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="escalation_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name">name*:</label>
      <input type="text" name="name" id="name" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'escalation_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="escalation_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'group_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="group,get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name">name*:</label>
      <input type="text" name="name" id="name" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'group_list': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="group_list" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="compatible">compatible:</label>
      <input type="text" name="compatible" id="compatible" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'group_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="group_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'role_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="role_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="name">name*:</label>
      <input type="text" name="name" id="name" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'role_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="role_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_getLastAlertFixedBy': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_getLastAlertFixedBy" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_find': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" ali11710gn="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_find" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="count">count*:</label>
      <input type="text" name="count" id="count" value="5000"/>
      <br />
      <label for="inEscalation">inEscalation:</label>
      <input type="text" name="inEscalation" id="inEscalation" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="severity">severity*:</label>
      <input type="text" name="severity" id="severity" value="3"/>
      <br />
      <label for="begin">begin*:</label>
      <input type="text" name="begin" id="begin" value="1349156415000"/>
      <br />
      <label for="notFixed">notFixed:</label>
      <input type="text" name="notFixed" id="notFixed" />
      <br />
      <label for="groupId">groupId:</label>
      <input type="text" name="groupId" id="groupId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_findByResource': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_findByResource" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="count">count*:</label>
      <input type="text" name="count" id="count"  value="5000"/>
      <br />
      <label for="begin">begin*:</label>
      <input type="text" name="begin" id="begin"  value="1349156415000"/>
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="severity">severity:</label>
      <input type="text" name="severity" id="severity" value="3"/>
      <br />
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <label for="inEscalation">inEscalation:</label>
      <input type="text" name="inEscalation" id="inEscalation" />
      <br />
      <label for="notFixed">notFixed:</label>
      <input type="text" name="notFixed" id="notFixed" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_ack': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_ack" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="reason">reason*:</label>
      <input type="text" name="reason" id="reason" />
      <br />
      <label for="pause">pause:</label>
      <input type="text" name="pause" id="pause" />
      <br />
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_fix': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_fix" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'alert_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="alert_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metricData_get': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metricData_get" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metricData_getLast': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metricData_getLast" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metricData_getMulti': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metricData_getMulti" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="start">start*:</label>
      <input type="text" name="start" id="start" />
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'metricData_getMultiLast': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="metricData_getMultiLast" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'event_find': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="event_find" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="count">count*:</label>
      <input type="text" name="count" id="count"  value="5000"/>
      <br />
      <label for="status">status:</label>
      <input type="text" name="status" id="status" />
      <br />
      <label for="begin">begin*:</label>
      <input type="text" name="begin" id="begin"  value="1349156415000"/>
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <label for="type">type:</label>
      <input type="text" name="type" id="type" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'event_findByResource': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="event_findByResource" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <label for="begin">begin*:</label>
      <input type="text" name="begin" id="begin"  value="1349156415000"/>
      <br />
      <label for="end">end*:</label>
      <input type="text" name="end" id="end" value="1356940842000"/>
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'control_actions': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="control_actions" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'control_history': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="control_history" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'control_execute': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="control_execute" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="action">action*:</label>
      <input type="text" name="action" id="action" />
      <br />
      <label for="resourceId">resourceId*:</label>
      <input type="text" name="resourceId" id="resourceId" />
      <br />
      <label for="arguments">arguments:</label>
      <input type="text" name="arguments" id="arguments" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
, 'application_delete': r'''
<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <fieldset align="right" style="width: 40%;">
      <input type="hidden" name="hidden" value="hidden" />
      <input type="hidden" name="actionName" value="application_delete" />
      <legend>Fields marked * are Necessary:</legend>
      <label for="id">id*:</label>
      <input type="text" name="id" id="id" />
      <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>
'''
,
'sql_serverResources': r'''<div class="form" align="center">
  <form action="/cgi-bin/hyperic-cli.py" method="POST" align="center">
    <input type="hidden" name="hidden" value="hidden" />
    <input type="hidden" name="actionName" value="sql_serverResources" />
    <fieldset align="right" style="width: 40%;">
    <input type="hidden" name="id" id="id" value="ignore"/>
    Get Platform information from Hyperic Database <br />
      <input type="submit" name="submit" id="submit" />
      <br />
    </fieldset>
  </form>
</div>'''
}


needed_fields = {
 'user_sync': ('xml_to_sync',), 
 'resource_sync': ('xml_to_sync',), 
}

def needed(_string):
  return needed_fields[_string]


from string import Template
def htmlmapper(_string, substring=None):
    if substring:
      return Template(htmlmap[_string]).safe_substitute({'data':substring})
    return htmlmap[_string]
