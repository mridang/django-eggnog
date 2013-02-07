def periodicallycheckforupdates():
    """
    Initialises and starts the advanced Python scheduler
    """
    try:
        from apscheduler.scheduler import Scheduler
    except ImportError, i:
        return
    else:
        sched = Scheduler()

        @sched.interval_schedule(seconds=10)
        def __check():
            """
            Periodically checks for updates
            """
            try:
                from django.core import management
                management.call_command('checkupdates', verbosity=0, interactive=False)
            except Exception, e:
                print e

        sched.start()
