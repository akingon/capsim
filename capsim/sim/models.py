from django.db import models
from json import dumps, loads
from .logic import Run, RunOutput


class RunRecord(models.Model):
    created = models.DateTimeField(auto_now=True)
    data = models.TextField(default=u"", blank=True, null=True)

    def get_run(self):
        return Run.from_dict(loads(self.data))

    def from_run(self, run):
        self.data = dumps(run.to_dict())
        self.save()


class RunOutputRecord(models.Model):
    created = models.DateTimeField(auto_now=True)
    run = models.ForeignKey(RunRecord)
    data = models.TextField(default=u"", blank=True, null=True)

    def from_runoutput(self, runoutput):
        self.data = dumps(runoutput.to_dict())
        self.save()

    def get_runoutput(self):
        d = loads(self.data)
        run = self.run.get_run()
        return RunOutput(
            ticks=d['ticks'], params=run.params, data=loads(d['data']))
