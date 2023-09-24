<template>
  <div
    id="graph"
    class="card"
  >
    <div class="card-header">
      <div class="row">
        <div class="col-8">
          <strong>Sub-basins</strong>
        </div>
        <div class="col-4">
          <div class="form-group">
            <v-select
              v-model="selectedSubBasin"
              :options="options"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="card-body no-padding">
      <b-tabs card>
        <b-tab title="Stream Flow">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <flowout-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <flowout-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Nitrate">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <no3-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <no3-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Dissolved Oxygen">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <disox-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <disox-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Sediment">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <sed-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <sed-out-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Total Nitrogen">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <totn-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <totn-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Total Phosphorus">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <totp-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <totp-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
        <b-tab title="Stream Temperature">
          <b-row>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Action Plan {{ $route.params.planId }}
              </h6>
              <wtmpdegc-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="false"
              />
            </b-col>
            <b-col
              lg="6"
            >
              <h6 class="baseline-graph-title text-center">
                Business as Usual
              </h6>
              <wtmpdegc-stream-sub-graph
                :selected-basin-id="selectedSubBasin.code"
                :base-graph="true"
              />
            </b-col>
          </b-row>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>
<script>

import GwqGraph from "@/components/dashboard/projects/charts/data/gwqGraph";
import WaterYieldGraph from "@/components/dashboard/projects/charts/data/waterYieldGraph";
import SedimentYieldGraph from "@/components/dashboard/projects/charts/data/sedimentYieldGraph";
import EtGraph from "@/components/dashboard/projects/charts/data/etGraph";
import SwGraph from "@/components/dashboard/projects/charts/data/swGraph";
import FlowoutStreamSubGraph from "@/components/dashboard/projects/charts/data/flowoutStreamSubGraph";
import No3OutStreamSubGraph from "@/components/dashboard/projects/charts/data/no3OutStreamSubGraph";
import DisoxOutStreamSubGraph from "@/components/dashboard/projects/charts/data/disoxOutStreamSubGraph";
import SedOutStreamSubGraph from "@/components/dashboard/projects/charts/data/sedOutStreamSubGraph";
import TotnStreamSubGraph from "@/components/dashboard/projects/charts/data/totnStreamSubGraph";
import TotpStreamSubGraph from "@/components/dashboard/projects/charts/data/totpStreamSubGraph";
import WtmpdegcStreamSubGraph from "@/components/dashboard/projects/charts/data/wtmpdegcStreamSubGraph";

export default {
  name: 'Actions',
  components: {
    WtmpdegcStreamSubGraph,
    TotpStreamSubGraph,
    TotnStreamSubGraph,
    SedOutStreamSubGraph,
    DisoxOutStreamSubGraph,
    No3OutStreamSubGraph,
    FlowoutStreamSubGraph, SwGraph, EtGraph, SedimentYieldGraph, WaterYieldGraph, GwqGraph,
  },
  props: {},
  data() {
    return {
      selectedSubBasin: {label: 'Sub-basin: 1', code: '1'},
      options: [
        {label: 'Sub-basin: 1', code: '1'},
        {label: 'Sub-basin: 2', code: '2'},
        {label: 'Sub-basin: 3', code: '3'},
        {label: 'Sub-basin: 4', code: '4'},
        {label: 'Sub-basin: 6', code: '6'},
        {label: 'Sub-basin: 7', code: '7'},
        {label: 'Sub-basin: 8', code: '8'},
        {label: 'Sub-basin: 9', code: '9'},
        {label: 'Sub-basin: 10', code: '10'},
        {label: 'Sub-basin: 11', code: '11'},
        {label: 'Sub-basin: 100', code: '100'},
        {label: 'Sub-basin: 101', code: '101'},
        {label: 'Sub-basin: 102', code: '102'},
        {label: 'Sub-basin: 103', code: '103'},
        {label: 'Sub-basin: 104', code: '104'},
        {label: 'Sub-basin: 105', code: '105'},
      ],
    };
  },
  watch: {},
  mounted() {

  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
