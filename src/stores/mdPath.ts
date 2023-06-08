import { defineStore } from 'pinia';
import { ref, Ref } from 'vue';

export const useMdPathStore = defineStore('mdPath', {
  state: (): State => {
    return {
      mdPath: {
        name: '',
        displayName: '',
        path: '',
        mds: [],
        nodes: [],
        nodeObjs: [],
        parent: null,
      },
    };
  },

  getters: {
    // doubleCount (state) {
    //   return state.counter * 2;
    // }
  },

  actions: {
    updateMdPath(data: MdPathModel) {
      this.mdPath = data;
    },
  },
});

interface State {
  mdPath: MdPathModel;
}
export interface MdPathModel {
  name: string;
  displayName: string;
  path: string;
  mds: Array<string>;
  mdFileInfos: Array<MdFileInfo>;
  nodes: Array<MdName>;
  nodeObjs: Array<MdPathModel>;
  parent: MdPathModel | null;
}
interface MdName {
  name: string;
  displayName: string;
}

interface MdFileInfo {
  name: string;
  title: string;
  path: string;
}
