#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot-methods/blob/master/LICENSE

import math
import numbers

import uproot_methods.base

class Methods(uproot_methods.base.ROOTMethods):

    @property
    def global_start_point(self):
        return self._global_5f_start_5f_point_5f_

    @property
    def global_end_point(self):
        return self._global_5f_end_5f_point_5f_

    @property
    def local_start_point(self):
        return self._local_5f_start_5f_point_5f_

    @property
    def local_end_point(self):
        return self._local_5f_end_5f_point_5f_

    @property
    def id(self):
        return self._particle_5f_id_5f_

    @property
    def parent(self):
        return self._parent_5f_

    @property
    def time(self):
        return self._time_5f_

    @property
    def track_reference(self):
        return self._track_5f_
