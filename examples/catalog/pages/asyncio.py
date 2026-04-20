import asyncio
import random
import ssl
import sys
import time

from utils import CODE_FONT_FAMILY
from flut.flutter.widgets import (
    StatefulWidget,
    StatelessWidget,
    State,
    Text,
    Column,
    Row,
    SizedBox,
    Container,
    Icon,
    TextEditingController,
    Navigator,
    RouteSettings,
    Center,
    Wrap,
)
from flut.flutter.rendering import CrossAxisAlignment, MainAxisSize
from flut.flutter.material import (
    Colors,
    ElevatedButton,
    Icons,
    CircularProgressIndicator,
    MaterialPageRoute,
    Scaffold,
    AppBar,
    Theme,
)
from flut.dart.ui import FontWeight
from flut.flutter.painting import (
    EdgeInsets,
    TextStyle,
    BorderRadius,
    BoxDecoration,
)
from flut.dart import Brightness, Color

from widgets import CatalogPage, SplitViewTile, CodeArea


def _build_log_widget(log_lines):
    widgets = []
    for line in log_lines:
        color = Colors.grey
        if line.startswith("\u2713"):
            color = Colors.green
        elif line.startswith("\u2717"):
            color = Colors.red
        elif line.startswith("\u25b6"):
            color = Colors.blue
        widgets.append(
            Text(
                line,
                style=TextStyle(fontSize=12, fontFamily=CODE_FONT_FAMILY, color=color),
            ),
        )
    if not widgets:
        widgets.append(
            Text(
                "No events yet.",
                style=TextStyle(fontSize=12, color=Colors.grey),
            ),
        )
    return Column(
        crossAxisAlignment=CrossAxisAlignment.start,
        children=widgets,
    )


def _build_status_row(status, elapsed):
    if status == "running":
        return Row(
            children=[
                SizedBox(width=16.0, height=16.0, child=CircularProgressIndicator()),
                SizedBox(width=8),
                Text(
                    "In progress...",
                    style=TextStyle(fontSize=13, color=Colors.orange),
                ),
            ]
        )
    if status == "success":
        return Row(
            children=[
                Icon(Icons.check_circle, color=Colors.green),
                SizedBox(width=8),
                Text(
                    f"Completed ({elapsed:.2f}s)",
                    style=TextStyle(fontSize=13, color=Colors.green),
                ),
            ]
        )
    if status == "timeout":
        return Row(
            children=[
                Icon(Icons.error, color=Colors.red),
                SizedBox(width=8),
                Text(
                    f"Timed out ({elapsed:.1f}s)",
                    style=TextStyle(fontSize=13, color=Colors.red),
                ),
            ]
        )
    if status == "error":
        return Row(
            children=[
                Icon(Icons.error, color=Colors.red),
                SizedBox(width=8),
                Text(
                    f"Error ({elapsed:.1f}s)",
                    style=TextStyle(fontSize=13, color=Colors.red),
                ),
            ]
        )
    return SizedBox()


class _CounterDemo(StatefulWidget):
    def createState(self):
        return _CounterDemoState()


class _CounterDemoState(State[_CounterDemo]):

    def initState(self):
        self.counter = 0
        self.delayed_counter = 0
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-10:]
        self.setState(lambda: None)

    def _increment_sync(self):
        self.counter += 1
        self._add_log(f"Sync increment \u2192 {self.counter}")

    async def _increment_delayed(self):
        async def _task():
            self._add_log("Waiting 1 second...")
            await asyncio.sleep(1)
            self.delayed_counter += 1
            self._add_log(f"Async increment \u2192 {self.delayed_counter}")
            self.setState(lambda: None)

        asyncio.create_task(_task())

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Sync +1"),
                            onPressed=self._increment_sync,
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Row(
                                children=[
                                    Icon(Icons.schedule),
                                    SizedBox(width=6),
                                    Text("Async +1 (1s)"),
                                ],
                            ),
                            onPressed=self._increment_delayed,
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"sync: {self.counter}  |  async: {self.delayed_counter}",
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _TimerDemo(StatefulWidget):
    def createState(self):
        return _TimerDemoState()


class _TimerDemoState(State[_TimerDemo]):

    def initState(self):
        self.stress_counter = 0
        self.stress_total = 0
        self.stress_running = False
        self.chain_step = 0
        self.chain_running = False
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-15:]
        self.setState(lambda: None)

    async def _run_stress_test(self):
        if self.stress_running:
            return

        self.stress_running = True
        self.stress_counter = 0
        self.stress_total = 50
        self._add_log(f"Stress test: {self.stress_total} timers (0.1\u201350ms)")

        async def _tick(delay_ms: float, index: int):
            await asyncio.sleep(delay_ms / 1000.0)
            self.stress_counter += 1
            if (
                self.stress_counter % 10 == 0
                or self.stress_counter == self.stress_total
            ):
                self._add_log(
                    f"  Timer {index} fired ({delay_ms:.1f}ms) \u2014 "
                    f"{self.stress_counter}/{self.stress_total}"
                )
            if self.stress_counter == self.stress_total:
                self.stress_running = False
                self._add_log("Stress test complete!")
            self.setState(lambda: None)

        for i in range(self.stress_total):
            delay = random.uniform(0.1, 50.0)
            asyncio.create_task(_tick(delay, i))

    async def _run_chained(self):
        if self.chain_running:
            return

        async def _chain():
            self.chain_running = True
            for step in range(1, 4):
                self.chain_step = step
                self._add_log(f"Chain step {step}/3...")
                await asyncio.sleep(0.5)
            self._add_log("Chain complete!")
            self.chain_running = False
            self.setState(lambda: None)

        asyncio.create_task(_chain())

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Row(
                                children=[
                                    Icon(Icons.speed),
                                    SizedBox(width=6),
                                    Text(f"Run {self.stress_total or 50} Timers"),
                                ],
                            ),
                            onPressed=(
                                None if self.stress_running else self._run_stress_test
                            ),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Text("Chained (3 steps)"),
                            onPressed=(
                                None if self.chain_running else self._run_chained
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                Text(
                    f"{self.stress_counter}/{self.stress_total or 0} completed"
                    + (
                        f"  |  chain: {self.chain_step}/3"
                        if self.chain_running
                        else ("  |  chain: done" if self.chain_step > 0 else "")
                    ),
                    style=TextStyle(fontSize=14),
                ),
            ],
        )


class _SocketIODemo(StatefulWidget):
    def createState(self):
        return _SocketIODemoState()


class _SocketIODemoState(State[_SocketIODemo]):

    def initState(self):
        self.io_status = "idle"
        self.io_elapsed = None
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-15:]
        self.setState(lambda: None)

    async def _run_socket_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            self._add_log("\u25b6 asyncio.open_connection('httpbin.org', 80)...")
            start = time.monotonic()
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection("httpbin.org", 80),
                    timeout=5.0,
                )
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "success"
                self._add_log(f"\u2713 Socket connected in {elapsed:.2f}s")
                writer.close()
            except asyncio.TimeoutError:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout"
                self._add_log(f"\u2717 Timed out after {elapsed:.1f}s")
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "error"
                self._add_log(f"\u2717 Error after {elapsed:.1f}s: {e}")

        asyncio.create_task(_go())

    async def _run_local_socket_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            self._add_log("\u25b6 asyncio.open_connection('127.0.0.1', 80)...")
            start = time.monotonic()
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection("127.0.0.1", 80),
                    timeout=5.0,
                )
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "success"
                self._add_log(f"\u2713 Connected in {elapsed:.2f}s")
                writer.close()
            except asyncio.TimeoutError:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout"
                self._add_log(f"\u2717 Timed out after {elapsed:.1f}s")
            except (ConnectionRefusedError, OSError) as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "success"
                self._add_log(
                    f"\u2713 Socket worked \u2014 port closed ({elapsed:.1f}s)"
                )
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "error"
                self._add_log(f"\u2717 Error after {elapsed:.1f}s: {e}")

        asyncio.create_task(_go())

    async def _run_subprocess_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            self._add_log("\u25b6 Subprocess: streaming 3 lines via readline()")

            script = (
                "import time, sys; "
                "["
                "(print(f'line {i}', flush=True), time.sleep(0.5)) "
                "for i in range(3)"
                "]"
            )

            start = time.monotonic()
            try:
                proc = await asyncio.wait_for(
                    asyncio.create_subprocess_exec(
                        sys.executable,
                        "-c",
                        script,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    ),
                    timeout=8.0,
                )
                lines_read = 0
                while True:
                    line = await asyncio.wait_for(
                        proc.stdout.readline(),
                        timeout=5.0,
                    )
                    if not line:
                        break
                    lines_read += 1
                    text = line.decode().strip()
                    self._add_log(
                        f"  Got '{text}' at t={time.monotonic() - start:.1f}s"
                    )

                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "success"
                self._add_log(f"\u2713 All {lines_read} lines in {elapsed:.1f}s")
                await proc.wait()
            except asyncio.TimeoutError:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout"
                self._add_log(f"\u2717 Timed out after {elapsed:.1f}s")
                try:
                    proc.kill()
                except Exception:
                    pass
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "error"
                self._add_log(f"\u2717 Error after {elapsed:.1f}s: {e}")

        asyncio.create_task(_go())

    def build(self, context):
        io_busy = self.io_status == "running"
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.cloud),
                                    SizedBox(width=6),
                                    Text("httpbin.org:80"),
                                ],
                            ),
                            onPressed=None if io_busy else self._run_socket_test,
                        ),
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.computer),
                                    SizedBox(width=6),
                                    Text("localhost:80"),
                                ],
                            ),
                            onPressed=(
                                None if io_busy else self._run_local_socket_test
                            ),
                        ),
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.terminal),
                                    SizedBox(width=6),
                                    Text("Subprocess"),
                                ],
                            ),
                            onPressed=(None if io_busy else self._run_subprocess_test),
                        ),
                    ],
                ),
                SizedBox(height=8),
                _build_status_row(self.io_status, self.io_elapsed),
            ],
        )


class _TlsHttpxDemo(StatefulWidget):
    def createState(self):
        return _TlsHttpxDemoState()


class _TlsHttpxDemoState(State[_TlsHttpxDemo]):

    def initState(self):
        self.io_status = "idle"
        self.io_elapsed = None
        self.log_lines = []
        self._cached_ssl_ctx = None
        self._cached_httpx_client = None

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-20:]
        self.setState(lambda: None)

    async def _run_tls_socket_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            start = time.monotonic()

            self._add_log("\u25b6 Phase 1: TCP connect to httpbin.org:443 (no ssl)...")
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection("httpbin.org", 443),
                    timeout=5.0,
                )
                tcp_elapsed = time.monotonic() - start
                self._add_log(f"  \u2713 TCP connected in {tcp_elapsed:.2f}s")
            except asyncio.TimeoutError:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout"
                self._add_log(f"\u2717 TCP connect timed out after {elapsed:.1f}s")
                return
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "error"
                self._add_log(f"\u2717 TCP error: {e}")
                return

            self._add_log("\u25b6 Phase 2: TLS handshake via loop.start_tls()...")
            try:
                import certifi

                ctx_start = time.monotonic()
                ctx = ssl.create_default_context(cafile=certifi.where())
                ctx_elapsed = time.monotonic() - ctx_start
                self._add_log(
                    f"  ssl.create_default_context(certifi) took {ctx_elapsed:.3f}s"
                )
            except ImportError:
                ctx_start = time.monotonic()
                ctx = ssl.create_default_context()
                ctx_elapsed = time.monotonic() - ctx_start
                self._add_log(f"  ssl.create_default_context() took {ctx_elapsed:.3f}s")
            tls_start = time.monotonic()
            try:
                transport = writer.transport
                protocol = transport.get_protocol()
                loop = asyncio.get_event_loop()
                new_transport = await asyncio.wait_for(
                    loop.start_tls(
                        transport, protocol, ctx, server_hostname="httpbin.org"
                    ),
                    timeout=10.0,
                )
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "success"
                self._add_log(
                    f"  \u2713 TLS handshake in {tls_elapsed:.2f}s (total {total:.2f}s)"
                )
                new_transport.close()
            except asyncio.TimeoutError:
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "timeout"
                self._add_log(
                    f"  \u2717 TLS handshake TIMEOUT after {tls_elapsed:.1f}s"
                )
                self._add_log(f"    TCP was fine \u2014 the TLS upgrade is what hangs")
                try:
                    writer.close()
                except Exception:
                    pass
            except Exception as e:
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "error"
                self._add_log(
                    f"  \u2717 TLS error after {tls_elapsed:.1f}s: {type(e).__name__}: {e}"
                )
                try:
                    writer.close()
                except Exception:
                    pass

        asyncio.create_task(_go())

    async def _run_httpx_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            try:
                import httpx
            except ImportError:
                self.io_status = "error"
                self._add_log("\u2717 httpx not installed (pip install httpx)")
                return
            self._add_log("\u25b6 httpx.AsyncClient GET https://httpbin.org/get ...")
            start = time.monotonic()
            try:
                async with httpx.AsyncClient(
                    timeout=httpx.Timeout(15.0, connect=10.0)
                ) as client:
                    r = await client.get("https://httpbin.org/get")
                    elapsed = time.monotonic() - start
                    self.io_elapsed = elapsed
                    self.io_status = "success"
                    self._add_log(f"\u2713 httpx {r.status_code} in {elapsed:.2f}s")
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout" if "Timeout" in type(e).__name__ else "error"
                self._add_log(
                    f"\u2717 httpx {type(e).__name__} after {elapsed:.1f}s: {e}"
                )

        asyncio.create_task(_go())

    async def _run_tls_cached_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            start = time.monotonic()

            self._add_log("\u25b6 TCP connect to httpbin.org:443...")
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection("httpbin.org", 443),
                    timeout=5.0,
                )
                tcp_elapsed = time.monotonic() - start
                self._add_log(f"  \u2713 TCP connected in {tcp_elapsed:.2f}s")
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "error"
                self._add_log(f"\u2717 TCP error: {e}")
                return

            if self._cached_ssl_ctx is None:
                self._add_log("  Creating SSLContext (first time)...")
                ctx_start = time.monotonic()
                try:
                    import certifi

                    self._cached_ssl_ctx = ssl.create_default_context(
                        cafile=certifi.where()
                    )
                except ImportError:
                    self._cached_ssl_ctx = ssl.create_default_context()
                ctx_elapsed = time.monotonic() - ctx_start
                self._add_log(
                    f"  ssl.create_default_context() took {ctx_elapsed:.3f}s (cached)"
                )
            else:
                self._add_log("  Reusing cached SSLContext")

            tls_start = time.monotonic()
            try:
                transport = writer.transport
                protocol = transport.get_protocol()
                loop = asyncio.get_event_loop()
                new_transport = await asyncio.wait_for(
                    loop.start_tls(
                        transport,
                        protocol,
                        self._cached_ssl_ctx,
                        server_hostname="httpbin.org",
                    ),
                    timeout=10.0,
                )
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "success"
                self._add_log(
                    f"  \u2713 TLS handshake in {tls_elapsed:.2f}s (total {total:.2f}s)"
                )
                new_transport.close()
            except asyncio.TimeoutError:
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "timeout"
                self._add_log(f"  \u2717 TLS TIMEOUT after {tls_elapsed:.1f}s")
                try:
                    writer.close()
                except Exception:
                    pass
            except Exception as e:
                tls_elapsed = time.monotonic() - tls_start
                total = time.monotonic() - start
                self.io_elapsed = total
                self.io_status = "error"
                self._add_log(
                    f"  \u2717 TLS error after {tls_elapsed:.1f}s: {type(e).__name__}: {e}"
                )
                try:
                    writer.close()
                except Exception:
                    pass

        asyncio.create_task(_go())

    async def _run_httpx_cached_test(self):
        if self.io_status == "running":
            return

        async def _go():
            self.io_status = "running"
            self.io_elapsed = None
            try:
                import httpx
            except ImportError:
                self.io_status = "error"
                self._add_log("\u2717 httpx not installed (pip install httpx)")
                return

            if self._cached_httpx_client is None:
                self._add_log("\u25b6 Creating httpx.AsyncClient (first time)...")
                ctx_start = time.monotonic()
                self._cached_httpx_client = httpx.AsyncClient(
                    timeout=httpx.Timeout(15.0, connect=10.0)
                )
                ctx_elapsed = time.monotonic() - ctx_start
                self._add_log(f"  Client created in {ctx_elapsed:.3f}s (cached)")
            else:
                self._add_log("\u25b6 Reusing cached httpx.AsyncClient")

            self._add_log("  GET https://httpbin.org/get ...")
            start = time.monotonic()
            try:
                r = await self._cached_httpx_client.get("https://httpbin.org/get")
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "success"
                self._add_log(f"\u2713 httpx {r.status_code} in {elapsed:.2f}s")
            except Exception as e:
                elapsed = time.monotonic() - start
                self.io_elapsed = elapsed
                self.io_status = "timeout" if "Timeout" in type(e).__name__ else "error"
                self._add_log(
                    f"\u2717 httpx {type(e).__name__} after {elapsed:.1f}s: {e}"
                )

        asyncio.create_task(_go())

    def build(self, context):
        io_busy = self.io_status == "running"
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Wrap(
                    spacing=8,
                    runSpacing=8,
                    children=[
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.lock),
                                    SizedBox(width=6),
                                    Text("TLS httpbin:443"),
                                ],
                            ),
                            onPressed=(None if io_busy else self._run_tls_socket_test),
                        ),
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.http),
                                    SizedBox(width=6),
                                    Text("httpx GET"),
                                ],
                            ),
                            onPressed=None if io_busy else self._run_httpx_test,
                        ),
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.lock),
                                    SizedBox(width=6),
                                    Text("TLS (cached ctx)"),
                                ],
                            ),
                            onPressed=(None if io_busy else self._run_tls_cached_test),
                        ),
                        ElevatedButton(
                            child=Row(
                                mainAxisSize=MainAxisSize.min,
                                children=[
                                    Icon(Icons.http),
                                    SizedBox(width=6),
                                    Text("httpx (cached)"),
                                ],
                            ),
                            onPressed=(
                                None if io_busy else self._run_httpx_cached_test
                            ),
                        ),
                    ],
                ),
                SizedBox(height=8),
                _build_status_row(self.io_status, self.io_elapsed),
            ],
        )


class _SyncDartReadDemo(StatefulWidget):
    def createState(self):
        return _SyncDartReadDemoState()


class _SyncDartReadDemoState(State[_SyncDartReadDemo]):

    def initState(self):
        self.test_controller = TextEditingController(text="hello")
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-10:]
        self.setState(lambda: None)

    async def _read_controller_text(self):
        async def _go():
            self._add_log("\u25b6 Reading controller.text from asyncio task...")
            text = self.test_controller.text
            self._add_log(f"\u2713 Got text = '{text}' (sync FFI from async context)")

        asyncio.create_task(_go())

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                ElevatedButton(
                    child=Row(
                        children=[
                            Icon(Icons.check_circle, color=Colors.green),
                            SizedBox(width=6),
                            Text("Read controller.text"),
                        ]
                    ),
                    onPressed=self._read_controller_text,
                ),
            ],
        )


class _FutureDemo(StatefulWidget):
    def createState(self):
        return _FutureDemoState()


class _FutureDemoState(State[_FutureDemo]):

    def initState(self):
        self.future_poll_result = None
        self.future_poll_ref = None
        self.future_then_result = None
        self.future_then_count = 0
        self.log_lines = []

    def _add_log(self, msg):
        self.log_lines = (self.log_lines + [msg])[-10:]
        self.setState(lambda: None)

    def _push_poll(self, context):
        self.future_poll_ref = Navigator.of(context).push(
            MaterialPageRoute(
                builder=lambda ctx: _FutureResultPage(title="Poll Demo"),
                settings=RouteSettings(name="/poll-demo"),
            ),
        )
        self.future_poll_result = None
        self.setState(lambda: None)

    def _check_poll(self):
        if self.future_poll_ref is None:
            return
        if self.future_poll_ref.isCompleted:
            self.future_poll_result = self.future_poll_ref.result
            self._add_log(f"Poll result: {self.future_poll_result}")
        else:
            self._add_log("Future not yet completed")
        self.setState(lambda: None)

    def _push_then(self, context):
        self.future_then_count += 1
        Navigator.of(context).push(
            MaterialPageRoute(
                builder=lambda ctx: _FutureResultPage(title=".then() Demo"),
                settings=RouteSettings(name="/then-demo"),
            ),
        ).then(self._on_then_result)

    def _on_then_result(self, result):
        self.future_then_result = result
        self._add_log(f".then() received: {result}")
        self.setState(lambda: None)

    def _format_poll_status(self):
        if self.future_poll_ref is None:
            return "(no future yet)"
        if self.future_poll_ref.isCompleted:
            return f"Completed: {self.future_poll_result}"
        return "Pending..."

    def build(self, context):
        return Column(
            crossAxisAlignment=CrossAxisAlignment.start,
            children=[
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Push & Store Future"),
                            onPressed=lambda: self._push_poll(context),
                        ),
                        SizedBox(width=12),
                        ElevatedButton(
                            child=Text("Check Future"),
                            onPressed=lambda: self._check_poll(),
                        ),
                    ],
                ),
                SizedBox(height=4),
                Text(
                    f"Poll: {self._format_poll_status()}",
                    style=TextStyle(fontSize=13, color=Colors.blue),
                ),
                SizedBox(height=8),
                Row(
                    children=[
                        ElevatedButton(
                            child=Text("Push & .then()"),
                            onPressed=lambda: self._push_then(context),
                        ),
                        SizedBox(width=12),
                        Text(
                            f".then() result: {self.future_then_result if self.future_then_result is not None else '(not yet)' if self.future_then_count == 0 else 'None'}",
                            style=TextStyle(fontSize=13, color=Colors.blue),
                        ),
                    ],
                ),
            ],
        )


class _FutureResultPage(StatefulWidget):
    def __init__(self, *, key=None, title="Pick a result"):
        super().__init__(key=key)
        self.title = title

    def createState(self):
        return _FutureResultPageState()


class _FutureResultPageState(State[_FutureResultPage]):

    def build(self, context):
        return Scaffold(
            appBar=AppBar(title=Text(self.widget.title)),
            body=Center(
                child=Column(
                    children=[
                        Text(
                            "Choose a value to pop back:",
                            style=TextStyle(fontSize=16),
                        ),
                        SizedBox(height=24),
                        ElevatedButton(
                            child=Text('Pop with "apple"'),
                            onPressed=lambda: Navigator.of(context).pop("apple"),
                        ),
                        SizedBox(height=12),
                        ElevatedButton(
                            child=Text('Pop with "banana"'),
                            onPressed=lambda: Navigator.of(context).pop("banana"),
                        ),
                        SizedBox(height=12),
                        ElevatedButton(
                            child=Text("Pop with None"),
                            onPressed=lambda: Navigator.of(context).pop(),
                        ),
                    ],
                ),
            ),
        )


class AsyncPage(StatelessWidget):
    def build(self, context):
        return CatalogPage(
            title="Async Support",
            description=(
                "Covers how Python async work cooperates with the UI loop, from "
                "delayed state updates and background tasks to streams, sockets, "
                "and calls that bridge into Dart-driven APIs."
            ),
            children=[
                SplitViewTile(
                    title="Sync vs Async Counter",
                    description=(
                        "Compares synchronous setState updates with async ones that "
                        "use asyncio.sleep to delay. Both correctly trigger rebuilds."
                    ),
                    instruction=(
                        "Click Sync +1 to increment immediately. "
                        "Click Async +1 (1s) and wait one second to see the delayed increment."
                    ),
                    visible=_CounterDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "async def increment_delayed():\n"
                            "    async def _task():\n"
                            "        await asyncio.sleep(1)\n"
                            "        counter += 1\n"
                            "        setState(lambda: None)\n"
                            "\n"
                            "    asyncio.create_task(_task())"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Timers",
                    description=(
                        "Fires many rapid asyncio timers to verify event-loop integration. "
                        "The stress test creates 50 concurrent timers with random delays "
                        "between 0.1ms and 50ms. Chained timers run sequentially."
                    ),
                    instruction=(
                        "Click 'Run 50 Timers' to launch the stress test and watch the "
                        "completion counter. Click 'Chained (3 steps)' to see sequential "
                        "async steps with 0.5s delays."
                    ),
                    visible=_TimerDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "async def tick(delay_ms, index):\n"
                            "    await asyncio.sleep(delay_ms / 1000.0)\n"
                            "    counter += 1\n"
                            "    setState(lambda: None)\n"
                            "\n"
                            "for i in range(50):\n"
                            "    delay = random.uniform(0.1, 50.0)\n"
                            "    asyncio.create_task(tick(delay, i))"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Socket I/O",
                    description=(
                        "Tests asyncio sockets and subprocesses through the platform I/O "
                        "bridge (IOCP on Windows, epoll on Linux, kqueue on macOS). "
                        "Buttons are disabled while a request is in flight."
                    ),
                    instruction=(
                        "Click 'httpbin.org:80' to open a remote TCP socket, "
                        "'localhost:80' to test a local connection, or 'Subprocess' to "
                        "stream lines from a child process via readline()."
                    ),
                    visible=_SocketIODemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "reader, writer = await asyncio.wait_for(\n"
                            "    asyncio.open_connection('httpbin.org', 80),\n"
                            "    timeout=5.0,\n"
                            ")\n"
                            "writer.close()"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="TLS & HTTPS",
                    description=(
                        "Tests TLS handshakes via loop.start_tls() and full HTTPS "
                        "requests via httpx. Cached variants reuse the SSLContext or "
                        "httpx.AsyncClient across calls to measure cold vs warm latency."
                    ),
                    instruction=(
                        "Click 'TLS httpbin:443' for a fresh TLS handshake, "
                        "'httpx GET' for a full HTTPS request, or the cached variants "
                        "to compare latency when reusing connections."
                    ),
                    visible=_TlsHttpxDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "transport = writer.transport\n"
                            "protocol = transport.get_protocol()\n"
                            "loop = asyncio.get_event_loop()\n"
                            "new_transport = await loop.start_tls(\n"
                            "    transport, protocol, ctx,\n"
                            "    server_hostname='httpbin.org',\n"
                            ")"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Sync Dart Reads from Async Context",
                    description=(
                        "controller.text uses sync FFI (call_dart). This works from "
                        "asyncio tasks because Flut auto-enters the Dart isolate when "
                        "needed, bridging Python's async world with Dart's synchronous API."
                    ),
                    instruction=(
                        "Click the button to read a TextEditingController's text from "
                        "inside an asyncio task. The log shows the sync FFI call succeeding."
                    ),
                    visible=_SyncDartReadDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "controller = TextEditingController(text='hello')\n"
                            "\n"
                            "async def read_text():\n"
                            "    async def _go():\n"
                            "        text = controller.text\n"
                            "    asyncio.create_task(_go())"
                        ),
                    ),
                ),
                SplitViewTile(
                    title="Future",
                    description=(
                        "Navigator.push returns a Future. Use .then(fn) for callback-style "
                        "handling or poll with .isCompleted / .result for manual checks."
                    ),
                    instruction=(
                        "Click 'Push & Store Future' to navigate, pick a value, then "
                        "come back and click 'Check Future' to poll the result. "
                        "Or click 'Push & .then()' to receive the result automatically."
                    ),
                    visible=_FutureDemo(),
                    code=CodeArea(
                        language="python",
                        code=(
                            "future = Navigator.of(context).push(\n"
                            "    MaterialPageRoute(\n"
                            "        builder=lambda ctx: ResultPage(),\n"
                            "    ),\n"
                            ")\n"
                            "\n"
                            "future.then(on_result)\n"
                            "\n"
                            "if future.isCompleted:\n"
                            "    value = future.result"
                        ),
                    ),
                ),
            ],
        )
