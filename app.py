from flask import Flask, render_template, request, make_response, jsonify
import dbQuery
import myService

app = Flask(__name__)

myService.worst_components_algo()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/components', methods=["GET", "POST"])
def components():
    response = dbQuery.listComponents()
    return render_template('component.html', response=response)


@app.route('/addComponent', methods=["GET", "POST"])
def addComponent():
    if (len(request.args) > 0):
        component_name = request.args.get('componentName')
        component_contact = request.args.get('componentContact')
        component_manufacturer = request.args.get('componentManufacturer')
        fail_rate = request.args.get('fail_rate')
        dbQuery.addComponents(component_name, component_contact, component_manufacturer, fail_rate)
        resp = dbQuery.listComponents()
        return render_template('component.html', response=resp)
    else:
        return render_template('addComponent.html')


@app.route('/removeComponent', methods=["GET", "POST"])
def removeComponent():
    component_id = request.args.get('id')
    msg = dbQuery.removeComponent(component_id)
    new_response = dbQuery.listComponents()
    return make_response(jsonify(component_id, 200))


@app.route('/updateComponent', methods=["GET", "POST"])
def updateComponent():
    if (len(request.args) > 0):
        component_id = request.args.get('componentID')
        component_name = request.args.get('componentName')
        component_contact = request.args.get('componentContact')
        component_manufacturer = request.args.get('componentManufacturer')
        fail_rate = request.args.get('fail_rate')
        dbQuery.updateComponent(component_id, component_name, component_contact, component_manufacturer, fail_rate)
        response = dbQuery.listComponents()
        return render_template('component.html', response=response)
    else:
        return render_template('updateComponent.html')


@app.route('/failmodes')
def failmodes():
    response = dbQuery.listFalmodes()
    return render_template('failmode.html', response=response)


@app.route('/addFailmode', methods=["GET", "POST"])
def addFailmode():
    if (len(request.args) > 0):
        failmode_name = request.args.get('failModeName')
        failmode_des = request.args.get('failModeDes')
        dbQuery.addFailMode(failmode_name, failmode_des)
        response = dbQuery.listFalmodes()
        return render_template('failmode.html', response=response)
    else:
        return render_template('addFailMode.html')


@app.route('/removeFailmode', methods=["GET", "POST"])
def removeFailmode():
    fm_id = request.args.get('id')
    msg = dbQuery.removeFailMode(fm_id)
    new_response = dbQuery.listFalmodes()
    return make_response(jsonify(fm_id, 200))


@app.route('/updateFailMode', methods=["GET", "POST"])
def updateFailMode():
    if (len(request.args) > 0):
        fm_id = request.args.get('failModeId')
        failmode_name = request.args.get('failModeName')
        failmode_des = request.args.get('failModeDes')
        dbQuery.updateFailMode(fm_id, failmode_name, failmode_des)
        response = dbQuery.listFalmodes()
        return render_template('failmode.html', response=response)
    else:
        return render_template('updateFailMode.html')


@app.route('/mappings')
def mappings():
    mp_response = dbQuery.listMappings()
    return render_template('mapping.html',
                           response=mp_response)


@app.route('/addMapping', methods=["GET", "POST"])
def addMapping():
    if (len(request.args) > 0):
        fail_code = request.args.get('failCode')
        component = request.args.get('component')
        fail_mode = request.args.get('failMode')
        dbQuery.addMapping(fail_code, component, fail_mode)
        response = dbQuery.listMappings()
        return render_template('mapping.html', response=response)
    else:
        mp_response = dbQuery.listMappings()
        fm_response = dbQuery.listFalmodes()
        co_response = dbQuery.listComponents()
        return render_template('addMapping.html', response={
            mappings: mp_response,
            components: co_response,
            failmodes: fm_response
        }, components=co_response, failmodes=fm_response)


@app.route('/removeMapping', methods=["GET", "POST"])
def removeMapping():
    mapping_id = request.args.get('id')
    msg = dbQuery.removeMapping(mapping_id)
    return make_response(jsonify(mapping_id, 200))


@app.route('/updateMapping', methods=["GET", "POST"])
def updateMapping():
    if (len(request.args) > 0):
        mapping_id = request.args.get('id')
        fail_code = request.args.get('failCode')
        component = request.args.get('component')
        fail_mode = request.args.get('failMode')
        dbQuery.updateMapping(mapping_id, fail_code, component, fail_mode)
        response = dbQuery.listMappings()
        return render_template('mapping.html', response=response)
    else:
        mp_response = dbQuery.listMappings()
        fm_response = dbQuery.listFalmodes()
        co_response = dbQuery.listComponents()
        return render_template('updateMapping.html', response={
            mappings: mp_response,
            components: co_response,
            failmodes: fm_response
        }, components=co_response, failmodes=fm_response)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/worstcomponents')
def worst_components():
    db_response = myService.worst_components_algo()
    return render_template('worstcomponents.html',
                           rows=db_response)


@app.route('/mostused')
def mostused():
    mu_response = myService.most_used_algo()
    return render_template('mostused.html',
                           rows=mu_response)


@app.route('/worstmanufacturer')
def worstmanufacturer():
    worstmanufacturer_response = myService.worst_manufacturer_algo()
    return render_template('worstmanufacturer.html',
                           rows=worstmanufacturer_response)


if __name__ == '__main__':
    app.run()
