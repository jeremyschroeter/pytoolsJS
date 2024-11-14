import os
import nrrd
import numpy as np
from allensdk.core.reference_space_cache import ReferenceSpaceCache, StructureTree
from pathlib import Path

class SimpleStructureTree:
    def __init__(self) -> None:
        self.tree = self._load_structure_tree()
        self.id_map = self.tree.get_name_map()
        self.name_map = {v : k for k, v in self.id_map.items()}
    
    def _load_structure_tree(self) -> StructureTree:
        output_dir = '.'
        reference_space_key = os.path.join('annotation', 'ccf_2017')
        resolution = 25
        rspc = ReferenceSpaceCache(resolution, reference_space_key, manifest=Path(output_dir) / 'manifest.json')
        tree = rspc.get_structure_tree(structure_graph_id=1)
        return tree

    def _clean_structure_dict(self, old_structure_dict: int) -> dict:
        structure_dict = {}
        id = old_structure_dict['id']
        structure_dict['id'] = id
        structure_dict['name'] = old_structure_dict['name']
        structure_dict['acronym'] = old_structure_dict['acronym']
        structure_dict['children'] = self.tree.child_ids([id])[0]
        structure_dict['ancestors'] = self.tree.ancestor_ids([id])[0][1:]
        return structure_dict
    
    def __getitem__(self, id) -> dict:
        if isinstance(id, str):
            id = self.name_map[id]
        return self._clean_structure_dict(self.tree.get_structures_by_id([id])[0])
    
    def collect_children(self, id) -> list:
        parent_dict = self.__getitem__(id)
        id = parent_dict['id']
        children = []
        for child_id in parent_dict['children']:
            children.extend(self.collect_children(child_id))
        if not children:
            children.append(id)
        return children
    

class AnnotationVolume:
    def __init__(self) -> None:
        self.av = self._load_av()
        self.tree = SimpleStructureTree()


    def _load_av(self):
        package_path = os.path.dirname(__file__)
        assets_path = os.path.join(package_path, 'assets')
        av_path = os.path.join(assets_path, 'annotation_10.nrrd')
        return nrrd.read(av_path)[0]

    def get_region_voxels(self, id, lowest: bool = True) -> np.ndarray:
        if isinstance(id, str):
            id = self.tree.name_map[id]
        if lowest is False:
            return np.array(np.where(np.isin(self.av, id))).T
        test_nodes = self.tree.collect_children(id)
        test_nodes.append(id)
        return np.array(np.where(np.isin(self.av, test_nodes))).T
    
    def __getitem__(self, index):
        return self.av[index]


