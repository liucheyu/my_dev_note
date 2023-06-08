<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-black text-white">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>Geek's Dev Note</q-toolbar-title>

        <!-- <div>Quasar v{{ $q.version }}</div> -->
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>
          <div
            @click="backToParent"
            class="cursor-pointer"
            :class="{ invisible: currentMdObj.parent == null }"
          >
            <q-icon :name="matArrowBack" size="sm"></q-icon
            ><span>(上一層)</span>
          </div>
        </q-item-label>

        <!-- <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        /> -->
        <template
          v-if="currentMdObj.mdFileInfos && currentMdObj.mdFileInfos.length > 0"
        >
          <q-item
            clickable
            :href="'#'"
            v-for="item in currentMdObj.mdFileInfos"
            :key="item.name"
            @click="setCurrentMdFile(item.path)"
          >
            <q-item-section>
              {{ item.title }}
            </q-item-section>
          </q-item>
        </template>
        <template v-if="currentMdObj.nodes && currentMdObj.nodes.length > 0">
          <q-item
            clickable
            @click="switchToNodes(item.name)"
            :href="'#'"
            v-for="item in currentMdObj.nodes"
            :key="item.name"
          >
            <q-item-section>
              {{ item.displayName }}
            </q-item-section>
          </q-item>
        </template>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page padding>
        <IndexPage v-if="openMdPage" :mdText="currentMdText" />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, nextTick } from 'vue';
import { storeToRefs } from 'pinia';
//import EssentialLink, { EssentialLinkProps } from 'components/EssentialLink.vue';
import IndexPage from 'pages/IndexPage.vue';
import YAML from 'yaml';
import { compileScript } from '@vue/compiler-sfc';
import { useMdPathStore } from 'stores/mdPath';
import { matArrowBack } from '@quasar/extras/material-icons';
import { $ } from 'app/dist/spa/assets/index.bd8668e9';

const MdPath = useMdPathStore();
const { mdPath } = storeToRefs(MdPath);

let currentMdObj = reactive(mdPath.value);

let currentMdFile = ref('');
let currentMdText = ref('');
let openMdPage = ref(false);

const switchToNodes = (nodeName: string) => {
  const temp = currentMdObj.nodeObjs.filter((ele) => ele.name == nodeName);

  if (temp && temp.length > 0) {
    let tmp = reactive({
      name: '',
      displayName: '',
      path: '',
      mds: [],
      mdFileInfos: [],
      nodes: [],
      nodeObjs: [],
      parent: null,
    });
    Object.assign(tmp, currentMdObj);
    Object.assign(currentMdObj, temp[0]);
    currentMdObj.parent = tmp;
    if (currentMdObj.mdFileInfos.length > 0) {
      setCurrentMdFile(currentMdObj.mdFileInfos[0].path);
    }
  }
};

const backToParent = () => {
  //todo 這裡也許可以有預設內容
  openMdPage.value = false;
  Object.assign(currentMdObj, currentMdObj.parent);
};

const setCurrentMdFile = (filePath: string) => {
  openMdPage.value = true;
  if (currentMdFile.value == filePath) {
    return;
  }

  currentMdFile.value = filePath;
  fetch(filePath).then((res) =>
    res.text().then((t) => {
      currentMdText.value = t;
    })
  );
};

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
