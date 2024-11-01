/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class OyRealtimeAction extends Component {
    static template = "oy_test_realtime.TemplateOyRealtime";

    setup() {
        this.state = useState({ count: 0 });
   
        this.env.services.bus_service.subscribe('realtime_oy_channel', (payload) => {
            console.log("MASUK BUS");
            this.state.count += 1;
        });
    }
}

registry.category("actions").add("oy_realtime_action", OyRealtimeAction);
