from research.model import project_hyperedges,global_efficiency,validate_bundle
def test_projection_and_efficiency():
    nodes=['a','b','c']; adj=project_hyperedges(nodes,[['a','b'],['b','c']]); assert adj['b']=={'a','c'}; assert round(global_efficiency(nodes,adj),4)==0.8333
def test_removal_can_reduce_efficiency():
    nodes=['a','b','c','d']; adj=project_hyperedges(nodes,[['a','b'],['b','c'],['c','d']]); assert global_efficiency(nodes,adj,{'b'})<global_efficiency(nodes,adj)
def test_packaged_curve(): assert validate_bundle()
